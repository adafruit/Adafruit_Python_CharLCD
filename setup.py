from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'Adafruit_CharLCD',
	  version 			= '1.0.0',
	  author			= 'Tony DiCola',
	  author_email		= 'tdicola@adafruit.com',
	  description		= 'Library to drive character LCD display and plate.',
	  license			= 'MIT',
	  url				= 'https://github.com/adafruit/Adafruit_Python_CharLCD/',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.4.0'],
	  install_requires	= ['Adafruit-GPIO>=0.4.0'],
	  packages 			= find_packages())
