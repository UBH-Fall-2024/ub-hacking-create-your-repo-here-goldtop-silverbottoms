from register_button import on_register_press
from verify_button import on_verify_press
from gpiozero import Button
from servo_power import servo_power

# Using BCM pin numbers
reg_button = Button(21)
ver_button = Button(20)
servo_power.off()
# mu = False

reg_result = 2

def button1():
    result = on_register_press()
    global reg_result
    if result == 1:
        reg_result = 1
    else: 
        reg_result = 2
    
def button2():
    if reg_result == 1:
        pass
    else:
        on_verify_press()

reg_button.when_pressed = button1
ver_button.when_pressed = button2

while True:
    pass