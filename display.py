# from RPLCD import CharLCD
# import RPi.GPIO as GPIO




# lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23], numbering_mode=GPIO.BOARD)
# lcd.write_string(u"Hello world")
from RPLCD.gpio import CharLCD
import lgpio


chip = lgpio.gpiochip_open(0)  # Opens the main GPIO chip (chip 0)

def setup(pin, direction):
    if direction == 'out':
        lgpio.gpio_claim_output(chip, pin)

def output(pin, value):
    lgpio.gpio_write(chip, pin, value)

def cleanup():
    lgpio.gpiochip_close(chip)

lcd = CharLCD(
    numbering_mode='BOARD',
    cols=16,
    rows=2,
    pin_rs=37,
    pin_e=35,
    pins_data=[40, 38, 36, 32, 33, 31, 29, 23],
    gpio=type('GPIOAdapter', (object,), {'setup': setup, 'output': output, 'cleanup': cleanup})()
)

# Write to the LCD
lcd.write_string(u"Hello world")