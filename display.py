from RPLCD import CharLCD
import RPi.GPIO as GPIO
from time import sleep

# Define LCD pin configuration
lcd = CharLCD(
    numbering_mode=GPIO.BCM,
    cols=16, rows=2,
    pin_rs=26, pin_rw=None, pin_e=19,
    pins_data=[13, 6, 5, 11]
)

# Initialize LCD and display a message
try:
    lcd.clear()
    lcd.write_string("Hello, World!")
    sleep(2)
    lcd.clear()
    lcd.write_string("Raspberry Pi LCD")
    sleep(2)
finally:
    lcd.clear()  # Clears the LCD display when done
    GPIO.cleanup()  # Clean up GPIO settings
