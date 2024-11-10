from register_button import on_register_press
from verify_button import on_verify_press
from gpiozero import Button
import servo_power

# Using BCM pin numbers
reg_button = Button(21)
ver_button = Button(20)
servo_power.servo_power.off()
servo_power.mu = False
reg_result = 2

def button1():
    if servo_power.mu == True:
        pass
    else:
        result = on_register_press()
        global reg_result
        if result == 1:
            reg_result = 1
        else: 
            reg_result = 2
        
def button2():
    if servo_power.mu == True:
        pass
    else:
        if reg_result == 1:
            pass
        else:
            on_verify_press()

reg_button.when_pressed = button1
ver_button.when_pressed = button2

while True:
    pass