from RPLCD.gpio import CharLCD
from gpiozero import DigitalOutputDevice
from time import sleep

# Set up the LCD using gpiozero's DigitalOutputDevice
lcd = CharLCD(
    numbering_mode='BOARD',         # Use physical pin numbering
    cols=16,                        # Number of columns on the LCD
    rows=2,                         # Number of rows on the LCD
    pin_rs=DigitalOutputDevice(37), # Register Select pin
    pin_e=DigitalOutputDevice(35),  # Enable pin
    pins_data=[
        DigitalOutputDevice(40),    # D0
        DigitalOutputDevice(38),    # D1
        DigitalOutputDevice(36),    # D2
        DigitalOutputDevice(32),    # D3
        DigitalOutputDevice(33),    # D4
        DigitalOutputDevice(31),    # D5
        DigitalOutputDevice(29),    # D6
        DigitalOutputDevice(23)     # D7
    ]
)

# Write a message to the LCD
lcd.write_string("Hello world!")

# Keep the message displayed for a while
sleep(5)

# Clear the display
lcd.clear()
