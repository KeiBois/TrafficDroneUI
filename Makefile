PYUIC5=/usr/bin/pyuic5
PYTHON=/home/ulimartinez/trafficdroneui/bin/python3.6
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