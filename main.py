radio.set_group(69)
cislo = 65
basic.show_string(String.from_char_code(cislo))
def on_button_pressed_a():
    global cislo
    if cislo == 65:
        basic.show_string(String.from_char_code(cislo))
    else:
        cislo -= 1
        basic.show_string(String.from_char_code(cislo))
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    global cislo
    if cislo == 90:
        basic.show_string(String.from_char_code(cislo))
    else:
        cislo += 1
        basic.show_string(String.from_char_code(cislo))
input.on_button_pressed(Button.B, on_button_pressed_b)
serials = control.device_serial_number()

def on_logo_event_pressed():
    radio.send_number(cislo-65)
    radio.send_number(serials)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

