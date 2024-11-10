import subprocess

def on_register_press():
    print("Register button pressed!")
    subprocess.call(["python3", "./register/face.py"])
    result = subprocess.call(["python3", "./register/encoder.py"])
    return result