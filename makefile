PYUIC5="/mnt/c/Users/erick/AppData/Local/Programs/Python/Python36/Scripts/pyuic5.exe"
UIFILES=window1
DIR=app/views/

all: $(UIFILES)

$(UIFILES): 
	 $(PYUIC5) -o $(DIR)$@.py $(DIR)$@.ui

clean: 
	rm app/views/$(UIFILES).py