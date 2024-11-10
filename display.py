from gpiozero import LED, Button, GPIOCharLCD
from time import sleep

# Initialize the LCD
lcd = GPIOCharLCD(
    rs=37,              # Register Select pin
    enable=35,          # Enable pin
    pins_data=[40, 38, 36, 32, 33, 31, 29, 23],  # Data pins D0-D7
    cols=16,            # Number of columns on the LCD
    rows=2,             # Number of rows on the LCD
    numbering_mode='BOARD'  # Use physical board numbering
)

# Display a message
lcd.write_string("Hello world!")

# Keep the message displayed for a while
sleep(5)

# Clear the display when done
lcd.clear()
