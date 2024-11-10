from RPLCD.gpio import CharLCD
import lgpio
import time

# Open the GPIO chip and define the chip number
chip = lgpio.gpiochip_open(0)  # Open GPIO chip 0

# Custom GPIO Interface
class GPIOAdapter:
    def setup(self, pin, direction):
        if direction == 'out':
            lgpio.gpio_claim_output(chip, pin)
        elif direction == 'in':
            lgpio.gpio_claim_input(chip, pin)

    def output(self, pin, value):
        lgpio.gpio_write(chip, pin, value)

    def cleanup(self):
        lgpio.gpiochip_close(chip)

# Initialize LCD with GPIO adapter
gpio_adapter = GPIOAdapter()

lcd = CharLCD(
    numbering_mode='BOARD',
    cols=16,
    rows=2,
    pin_rs=37,
    pin_e=35,
    pins_data=[40, 38, 36, 32, 33, 31, 29, 23],
    pin_rw=None,  # Set to None if not used
    gpio=gpio_adapter
)

# Write a message to the LCD
lcd.write_string(u"Hello world!")

# Keep the message displayed for a while
time.sleep(5)

# Clear and release resources
lcd.clear()
gpio_adapter.cleanup()
