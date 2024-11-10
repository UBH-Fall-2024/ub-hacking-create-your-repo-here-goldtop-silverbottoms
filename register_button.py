import subprocess
# from servo_power import mu

# mu = True
def on_register_press():
    print("Register button pressed!")
    subprocess.call(["python3", "./register/face.py"])
    result = subprocess.call(["python3", "./register/encoder.py"])
    # mu = False
    return result