from register_button import on_register_press
from verify_button import on_verify_press
from gpiozero import Button

reg_button = Button(21)
ver_button = Button(20)

def button1():
    on_register_press
    
def button2():
    on_verify_press

# def buttons(button_number):
#     if button_number == 21: # register case
#         on_register_press()
#     elif button_number == 20:
#         on_verify_press()

reg_button.when_pressed = button1
ver_button.when_pressed = button2

while True:
    pass