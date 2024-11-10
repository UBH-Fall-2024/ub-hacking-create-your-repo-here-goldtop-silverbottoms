from gpiozero import Button, Device
from gpiozero.pins.mock import MockFactory
import subprocess


# Enable Mock mode
# Device.pin_factory = MockFactory()

button = Button(40) # put number of GPIO pin in function

def on_register_press():
    print("Register button pressed!")
    subprocess.call(["python3", "./register/face.py"])
    subprocess.call(["python3", "./register/encoder.py"])
    
button.when_activated = on_register_press