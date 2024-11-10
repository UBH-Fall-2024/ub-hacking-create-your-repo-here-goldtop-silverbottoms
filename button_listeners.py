from register_button import on_register_press
from verify_button import on_verify_press
from gpiozero import Button

reg_button = Button(21)
ver_button = Button(20)

def buttons(button_number):
    if button_number == 21: # register case
        on_register_press()
    elif button_number == 20:
        on_verify_press()

reg_button.when_pressed = buttons(21)
ver_button.when_pressed = buttons(20)

while True:
    pass