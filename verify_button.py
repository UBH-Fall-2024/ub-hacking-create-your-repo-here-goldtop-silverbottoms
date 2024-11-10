from gpiozero import Servo, PWMLED
from time import sleep
import subprocess
import servo_power

servo_power.mu = True
servo = Servo(17)
red_light = PWMLED(26)
green_light = PWMLED(19)

def on_verify_press():
    print("Verify button pressed!")
    subprocess.call(["python3", "./verify/facial.py"])
    result = subprocess.call(["python3", "./verify/compare.py"])
    if result == 0:
        servo_power.servo_power.on()
        green_light.value = 1
        print("Face verified from button press!\nSpinning motor...")
        servo.max()
        sleep(5)
        servo.min()
        print("Motor stopped.")
        green_light.value = 0
        servo_power.servo_power.off()
        servo_power.mu = False
    else:
        print("Face not verified from button press. Motor won't spin.")
        red_light.value = 1
        sleep(3)
        red_light.value = 0
        servo_power.mu = False