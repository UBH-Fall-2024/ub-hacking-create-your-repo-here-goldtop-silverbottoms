import subprocess
import servo_power

servo_power.mu = True
def on_register_press():
    print("Register button pressed!")
    subprocess.call(["python3", "./register/face.py"])
    result = subprocess.call(["python3", "./register/encoder.py"])
    servo_power.mu = False
    return result