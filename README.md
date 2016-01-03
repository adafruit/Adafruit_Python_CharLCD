Adafruit_Python_CharLCD
=======================

Python library for accessing Adafruit character LCDs from a Raspberry Pi or BeagleBone Black.

Designed specifically to work with the Adafruit character LCDs ----> https://learn.adafruit.com/character-lcds/overview

For all platforms (Raspberry Pi and Beaglebone Black) make sure you have the following dependencies:

````
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus python-pip
````

For a Raspberry Pi make sure you have the RPi.GPIO library by executing:

````
sudo pip install RPi.GPIO
````

For a BeagleBone Black make sure you have the Adafruit_BBIO library by executing:

````
sudo pip install Adafruit_BBIO
````

Install the library by downloading with the download link on the right, unzipping the archive, navigating inside the library's directory and executing:

````
sudo python setup.py install
````

See example of usage in the examples folder.

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.

MIT license, all text above must be included in any redistribution
