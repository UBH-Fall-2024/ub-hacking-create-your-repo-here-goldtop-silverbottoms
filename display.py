import time
import gpiod
import adafruit_character_lcd.character_lcd as character_lcd

# Define the LCD pin configuration using BCM pin numbering
lcd_columns = 16  # Set the number of columns (16x2 LCD)
lcd_rows = 2      # Set the number of rows (16x2 LCD)

# Define BCM GPIO pin numbers
rs = 26  # RS pin (GPIO 26)
en = 19  # Enable pin (GPIO 19)
d4 = 13  # Data pin (GPIO 13)
d5 = 6   # Data pin (GPIO 6)
d6 = 5   # Data pin (GPIO 5)
d7 = 11  # Data pin (GPIO 11)

# Setup GPIO via gpiod (libgpiod)
chip = gpiod.Chip('0')  # GPIO chip (usually '0' for Raspberry Pi)
rs_line = chip.get_line(rs)
en_line = chip.get_line(en)
d4_line = chip.get_line(d4)
d5_line = chip.get_line(d5)
d6_line = chip.get_line(d6)
d7_line = chip.get_line(d7)

# Set lines to output
rs_line.request(consumer="lcd", type=gpiod.LINE_REQ_DIR_OUT)
en_line.request(consumer="lcd", type=gpiod.LINE_REQ_DIR_OUT)
d4_line.request(consumer="lcd", type=gpiod.LINE_REQ_DIR_OUT)
d5_line.request(consumer="lcd", type=gpiod.LINE_REQ_DIR_OUT)
d6_line.request(consumer="lcd", type=gpiod.LINE_REQ_DIR_OUT)
d7_line.request(consumer="lcd", type=gpiod.LINE_REQ_DIR_OUT)

# Initialize the LCD using the GPIO lines
lcd = character_lcd.Character_LCD_Mono(rs_line, en_line, d4_line, d5_line, d6_line, d7_line, lcd_columns, lcd_rows)

# Print a message on the LCD
lcd.clear()
lcd.message = "Hello, World!"

# Wait for a few seconds and then clear the screen
time.sleep(3)
lcd.clear()

# Cleanup (optional, as libgpiod automatically cleans up when the script finishes)
