PYUIC5=/mnt/c/Users/erick/AppData/Local/Programs/Python/Python36/Scripts/pyuic5.exe
PYTHON=/mnt/c/Users/erick/AppData/Local/Programs/Python/Python36/python.exe
UIFILES=window1 MapView DashBoard TrafficAlerts
DIR=app/controllers/views/

all: $(UIFILES)

$(UIFILES): 
	 $(PYUIC5) -o $(DIR)$@.py $(DIR)$@.ui

clean:
	rm $(DIR)*.py
	touch $(DIR)__init__.py

run: all
	$(PYTHON) app/main.py