import imageProcessing as ip
import numpy as np
import cv2
import helper as aux
from moviepy.editor import ImageSequenceClip, VideoFileClip
import os.path
from tqdm import tqdm
from scanner import VehicleScanner


class Detector:
    def __init__(self, imgMarginWidth=320, historyDepth=5, margin=100, windowSplit=2, winCount=9,
                 searchPortion=1., veHiDepth=30, pointSize=64,
                 groupThrd=10, groupDiff=.1, confidenceThrd=.7):
        self.imgProcessor = ip.Processing()
        self.warper = ip.Warping()
        self.imgMarginWidth = imgMarginWidth
        self.fitHistory = []

        # ====| PROJECT 5 - VEHICLE DETECTION |====
        # Adding Vehicle scanner
        self.scanner = VehicleScanner(pointSize=pointSize,
                                      veHiDepth=veHiDepth, groupThrd=groupThrd, groupDiff=groupDiff,
                                      confidenceThrd=confidenceThrd)

    def preProcess(self, src):
        """
        Creates binary with combined threshold and applies
        perspective transform for bird-eye view
        :param src: source color image (assuming it's been previously undistorted)
        :return: bird-eye view binary
        """
        imgHeight = src.shape[0]

        binary = ip.Thresholding.combiThreshold(src=src)

        filler = np.zeros((imgHeight, self.imgMarginWidth), dtype=np.uint8)
        binary = np.hstack((filler, binary, filler))

        binaryWarp = self.warper.birdEye(img=binary, leftShift=self.imgMarginWidth)

        return binaryWarp

    @staticmethod
    def sanityCheckPass(fitL, fitR):
        """
        Checking for left and right curvatures similarity and lane width to be within a given range
        :param fitL: left curve polynomial parameters
        :param fitR: right curve polynomial parameters
        :return: True or False
        """
        tolerance = 1.2
        maxCurvDelta = 0.006  # 0.000666 * tolerance
        laneWidthRange = (800 / tolerance, 1000 * tolerance)
        imgBottom = 719

        if fitR is None or fitL is None:
            return False

        al = fitL[0]
        ar = fitR[0]

        curvDelta = abs(ar - al)
        if curvDelta > maxCurvDelta:
            return False
        else:

            bl = fitL[1]
            br = fitR[1]

            cl = fitL[2]
            cr = fitR[2]

            leftBottomX = al * (imgBottom ** 2) + bl * imgBottom + cl
            rightBottomX = ar * (imgBottom ** 2) + br * imgBottom + cr

            laneWidth = rightBottomX - leftBottomX

            return (rightBottomX > leftBottomX) & (
                laneWidthRange[1] >= laneWidth >= int(laneWidthRange[0]))

    def addLanePoly(self, srcShape, dst, fitLeft, fitRight):
        """
        Adding lane polygon to an empty image with the shape of bird-eye view with 
        subsequent perspective projection to destination image (clipping previously added left and right fillers)
        :param srcShape: shape of bird-eye view (may be wider than original image)
        :param dst: original color (assumed previously undistorted) image
        :param fitLeft: left curve polynomial parameters
        :param fitRight: right curve polynomial parameters
        :return: color image with projected lane
        """
        lanePolyImg, leftOutstand, _ = ip.Drawing.addPolygon(srcShape=srcShape, lFit=fitLeft,
                                                             rFit=fitRight, stepCount=10, color=(0, 255, 0))
        imgH = dst.shape[1]

        lShift = self.imgMarginWidth + leftOutstand
        perspective = self.warper.perspective(lanePolyImg,
                                              leftShift=lShift)[:, lShift:lShift + imgH, :]
        return cv2.addWeighted(dst, 1, perspective, 0.5, 0)

    def addPip(self, pipImage, dstImage, pipAlpha=0.5, pipResizeRatio=0.3, origin=(20, 20)):
        """
        Adding small Picture-in-picture binary bird-eye projection with search areas and found lines embedded
        :param pipImage: original binary bird-eye projection with search areas and found lines embedded
        :param dstImage: destination color image (assumed undistorted)
        :param pipAlpha: pip alpha
        :param pipResizeRatio: pip scale
        :param origin: coordinates of upper-left corner of small picture
        :return: color image with P-i-P embedded
        """
        smallPip = self.imgProcessor.resize(src=pipImage, ratio=pipResizeRatio)

        pipHeight = smallPip.shape[0]
        pipWidth = smallPip.shape[1]

        backGround = dstImage[origin[1]:origin[1] + pipHeight, origin[0]:origin[0] + pipWidth]

        blend = np.round(backGround * (1 - pipAlpha), 0) + np.round(smallPip * pipAlpha, 0)

        blend = np.minimum(blend, 255)

        dstImage[origin[1]:origin[1] + pipHeight, origin[0]:origin[0] + pipWidth] = blend

        # return dstImage

    def addOffsetStamp(self, leftFit, rightFit, image, origin, color=(255, 255, 255), fontScale=1.0, thickness=1):
        """
        Evaluating camera offset and adding it to a given image
        :param thickness: line thickness
        :param leftFit: left curve polynomial parameters
        :param rightFit: right curve polynomial parameters
        :param image: image where data being added
        :param origin: upper-left corner of the offset stamp
        :param color: stamp color
        :param fontScale: font scale
        :return: void (adds text to passed image)
        """

        imgW = image.shape[1]
        imgH = image.shape[0]

        yBottom = imgH - 1
        cameraCenter = imgW / 2
        lBottomX = aux.funcSpace(argSpace=yBottom, fitParams=leftFit) - self.imgMarginWidth
        rBottomX = aux.funcSpace(argSpace=yBottom, fitParams=rightFit) - self.imgMarginWidth
        laneWidth = rBottomX - lBottomX
        scaleX = 3.7 / laneWidth
        laneCenter = (lBottomX + rBottomX) / 2
        offSet = (cameraCenter - laneCenter) * scaleX
        aux.putText(img=image, text='Estimated Vehicle Offset: {:.2f} m'.format(offSet),
                    origin=origin, color=color, scale=fontScale, thickness=thickness)

    @staticmethod
    def addCurvatureStamp(leftFit, rightFit, image, origin, color=(255, 255, 255), fontScale=1.0, thickness=1):

        """
        Evaluating lane curvature and adding it to a given image
        :param thickness: text thickness
        :param leftFit: left curve polynomial parameters
        :param rightFit: right curve polynomial parameters
        :param image: image where data being added
        :param origin: upper-left corner of the offset stamp
        :param color: stamp color
        :param fontScale: font scale
        :return: void (adds text to passed image)
        """

        imgH = image.shape[0]

        yBottom = imgH - 1
        scaleY = 27 / imgH  # meters per pixel
        leftCurvature = aux.curvature(fitParams=leftFit, variable=yBottom, scale=scaleY)
        rightCurvature = aux.curvature(fitParams=rightFit, variable=yBottom, scale=scaleY)
        curvature = (leftCurvature + rightCurvature) / 2
        aux.putText(img=image, text='Estimated Lane Curvature: {:.1f} m'.format(round(curvature / 100, 1) * 100),
                    origin=origin, color=color, scale=fontScale, thickness=thickness)

    def embedDetections(self, src, pipParams=None):
        """
        Main 'pipeline' for adding Lane polygon AND detected vehicles to the original image
        :param src: original image
        :param pipParams: alpha and scale ratios
        :return: undistorted color image with the Lane embedded.
        """

        # 1. Undistortion
        img = self.imgProcessor.undistort(src=src)

        """
        1a. ====| PROJECT 5 - VEHICLE DETECTION |====
        Getting vehicle boxes
        """
        vBoxes, heatMap = self.scanner.relevantBoxes(src=img)

        # 2. Binary (bird-eye projection)
        binary = self.preProcess(src=img)

        # ====| PROJECT 5 - VEHICLE DETECTION |====
        # Drawing vehicle boxes
        aux.drawBoxes(img=img, bBoxes=vBoxes)

        # Upper left corner where starting to add pip and telemetry
        origin = (20, 20)

        # Adding PIP
        if pipParams is not None:
            alpha = pipParams['alpha']
            ratio = pipParams['scaleRatio']


            # To keep for subsequent telemetry stamps
            heatWidth = int(heatMap.shape[1] * ratio)

            # Lane Detection Picture-in-Picture


            # ====| PROJECT 5 - VEHICLE DETECTION |====
            # Vehicle Detection Picture-in-Picture
            self.addPip(pipImage=heatMap, dstImage=img,
                        pipAlpha=alpha, pipResizeRatio=ratio,
                        origin=(img.shape[1] - heatWidth - 20, 20))

        return img


def main():
    """
    Runs when invoking directly from command line
    :return: 
    """
    resultFrames = []

    clipFileName = input('Enter video file name: ')

    if not os.path.isfile(clipFileName):
        print('No such file. Exiting.')
        return

    clip = VideoFileClip(clipFileName)

    # depth = aux.promptForInt(message='Enter history depth in frames: ')
    # detectionPointSize = aux.promptForInt(message='Enter Search Margin: ')
    # fillerWidth = aux.promptForInt(message='Enter filler width: ')
    # windowSplit = aux.promptForInt(message='Enter Window Split: ')
    # winCount = aux.promptForInt(message='Enter Window Count for Box Search: ')
    # searchPortion = aux.promptForFloat(message='Enter the Search portion (0.0 - 1.0): ')
    # pipAlpha = aux.promptForFloat(message='Enter Picture-in-picture alpha: (0.0 - 1.0): ')
    # pipScaleRatio = aux.promptForFloat(message='Enter Picture-in-picture scale (0.0 - 1.0): ')

    depth = 5
    margin = 100
    fillerWidth = 320
    windowSplit = 2
    winCount = 18
    searchPortion = 1.

    pipAlpha = .7
    pipScaleRatio = .35

    pipParams = {'alpha': pipAlpha, 'scaleRatio': pipScaleRatio}

    print('Total frames: {}'.format(clip.duration * clip.fps))

    ld = Detector(imgMarginWidth=fillerWidth, historyDepth=depth,
                  margin=margin, windowSplit=windowSplit, winCount=winCount,
                  searchPortion=searchPortion, veHiDepth=45,
                  pointSize=64, groupThrd=10, groupDiff=.1, confidenceThrd=.5)

    for frame in tqdm(clip.iter_frames()):
        dst = ld.embedDetections(src=frame, pipParams=pipParams)
        resultFrames.append(dst)

    resultClip = ImageSequenceClip(resultFrames, fps=25, with_mask=False)
    resultFileName = clipFileName.split('.')[0]
    resultFileName = '{}_out_{}.mp4'.format(resultFileName, aux.timeStamp())
    resultClip.write_videofile(resultFileName, progress_bar=True)


if __name__ == '__main__':
    main()
