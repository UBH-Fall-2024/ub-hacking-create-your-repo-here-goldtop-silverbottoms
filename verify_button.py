from gpiozero import Button, Device, Servo
from gpiozero.pins.mock import MockFactory
from time import sleep
import subprocess
from RPLCD import CharLCD


servo = Servo(17)

def on_verify_press():
    print("Verify button pressed!")
    subprocess.call(["python3", "./verify/facial.py"])
    result = subprocess.call(["python3", "./verify/compare.py"])
    if result == 0:
        # lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[])
        # lcd.write_string(u"Hello world")
        print("Face verified from button press!\nSpinning motor...")
        for _ in range(1):
            servo.max()
            sleep(0.5)
            servo.min()
            sleep(0.5)
        
        servo.mid()
        print("Motor stopped.")
    else:
        print("Face not verified from button press. Motor won't spin.")
        
