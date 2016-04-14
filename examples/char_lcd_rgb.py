#!/usr/bin/python
# Example using an RGB character LCD wired directly to Raspberry Pi or BeagleBone Black.
import time

import Adafruit_CharLCD as LCD


# Raspberry Pi configuration:
lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_red   = 4
lcd_green = 17
lcd_blue  = 7  # Pin 7 is CE1

# BeagleBone Black configuration:
# lcd_rs = 'P8_8'
# lcd_en = 'P8_10'
# lcd_d4 = 'P8_18'
# lcd_d5 = 'P8_16'
# lcd_d6 = 'P8_14'
# lcd_d7 = 'P8_12'
# lcd_red   = 'P8_7'
# lcd_green = 'P8_9'
# lcd_blue  = 'P8_11'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                              lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)

# Show some basic colors.
lcd.set_color(1.0, 0.0, 0.0)
lcd.clear()
lcd.message('RED')
time.sleep(3.0)

lcd.set_color(0.0, 1.0, 0.0)
lcd.clear()
lcd.message('GREEN')
time.sleep(3.0)

lcd.set_color(0.0, 0.0, 1.0)
lcd.clear()
lcd.message('BLUE')
time.sleep(3.0)

lcd.set_color(1.0, 1.0, 0.0)
lcd.clear()
lcd.message('YELLOW')
time.sleep(3.0)

lcd.set_color(0.0, 1.0, 1.0)
lcd.clear()
lcd.message('CYAN')
time.sleep(3.0)

lcd.set_color(1.0, 0.0, 1.0)
lcd.clear()
lcd.message('MAGENTA')
time.sleep(3.0)

lcd.set_color(1.0, 1.0, 1.0)
lcd.clear()
lcd.message('WHITE')
time.sleep(3.0)
