radio.setGroup(69)
let cislo = 65
basic.showString(String.fromCharCode(cislo))
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (cislo == 65) {
        basic.showString(String.fromCharCode(cislo))
    } else {
        cislo -= 1
        basic.showString(String.fromCharCode(cislo))
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (cislo == 90) {
        basic.showString(String.fromCharCode(cislo))
    } else {
        cislo += 1
        basic.showString(String.fromCharCode(cislo))
    }
    
})
let serials = control.deviceSerialNumber()
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    radio.sendNumber(cislo - 65)
    radio.sendNumber(serials)
})
