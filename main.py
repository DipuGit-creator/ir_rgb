function toggleMode () {
    if (code == 144 && mode == 1) {
        mode = 0
    } else if (code == 144 && mode == 0) {
        mode = 1
    }
}
function randomColorStep () {
    r = randint(0, 1023)
    g = randint(0, 1023)
    b = randint(0, 1023)
    pins.analogWritePin(AnalogPin.P5, 1023 - r)
    pins.analogWritePin(AnalogPin.P6, 1023 - g)
    pins.analogWritePin(AnalogPin.P7, 1023 - b)
}
let start = 0
let discoMode = false
let SELECTED_COLOR = 0
let P7x = 0
let P6x = 0
let P5x = 0
let whitex = 0
let b = 0
let g = 0
let r = 0
let code = 0
let mode = 0
led.enable(false)
// === Setup IR receiver on pin P0 ===
irVS1838.connectIrReceiver(DigitalPin.P2)
mode = 0
// === Main loop: check for a new IR code ===
basic.forever(function () {
    if (irVS1838.wasIrDataReceived()) {
        // ready for the next press
        code = irVS1838.irButton()
        // === Map each code to its button name ===
        if (code == 162) {
        	
        } else if (code == 98) {
        	
        } else if (code == 226) {
        	
        } else if (code == 34) {
        	
        } else if (code == 2) {
        	
        } else if (code == 194) {
            pins.analogWritePin(AnalogPin.P7, 1023)
            pins.analogWritePin(AnalogPin.P5, 1023)
            pins.analogWritePin(AnalogPin.P6, 1023)
            whitex = 0
            P5x = 0
            P6x = 0
            P7x = 0
            SELECTED_COLOR = 9999
        } else if (code == 224) {
            if (mode == 1 && SELECTED_COLOR == 0) {
                P5x += 50
                pins.analogWritePin(AnalogPin.P5, P5x)
            } else if (mode == 1 && SELECTED_COLOR == 1) {
                P6x += 50
                pins.analogWritePin(AnalogPin.P6, P6x)
            } else if (mode == 1 && SELECTED_COLOR == 2) {
                P7x += 50
                pins.analogWritePin(AnalogPin.P7, P7x)
            } else if (mode == 1 && SELECTED_COLOR == -1) {
                whitex += 50
                pins.analogWritePin(AnalogPin.P5, whitex)
                pins.analogWritePin(AnalogPin.P6, whitex)
                pins.analogWritePin(AnalogPin.P7, whitex)
            }
        } else if (code == 168) {
            if (mode == 1 && SELECTED_COLOR == 0) {
                P5x += -50
                pins.analogWritePin(AnalogPin.P5, P5x)
            } else if (mode == 1 && SELECTED_COLOR == 1) {
                P6x += -50
                pins.analogWritePin(AnalogPin.P6, P6x)
            } else if (mode == 1 && SELECTED_COLOR == 2) {
                P7x += -50
                pins.analogWritePin(AnalogPin.P7, P7x)
            } else if (mode == 1 && SELECTED_COLOR == -1) {
                whitex += -50
                pins.analogWritePin(AnalogPin.P5, whitex)
                pins.analogWritePin(AnalogPin.P6, whitex)
                pins.analogWritePin(AnalogPin.P7, whitex)
            }
        } else if (code == 144) {
            toggleMode()
            pins.analogWritePin(AnalogPin.P7, 1023)
            pins.analogWritePin(AnalogPin.P5, 1023)
            pins.analogWritePin(AnalogPin.P6, 1023)
            whitex = 0
            P5x = 0
            P6x = 0
            P7x = 0
            SELECTED_COLOR = 9999
        } else if (code == 104) {
            pins.analogWritePin(AnalogPin.P7, 0)
            pins.analogWritePin(AnalogPin.P5, 0)
            pins.analogWritePin(AnalogPin.P6, 0)
            SELECTED_COLOR = -1
        } else if (code == 152) {
        	
        } else if (code == 176) {
        	
        } else if (code == 48) {
            if (mode == 0) {
                pins.analogWritePin(AnalogPin.P7, 1023)
                pins.analogWritePin(AnalogPin.P5, 0)
                pins.analogWritePin(AnalogPin.P6, 1023)
            } else if (mode == 1) {
                pins.analogWritePin(AnalogPin.P5, 0)
            }
            P5x = 0
            SELECTED_COLOR = 0
        } else if (code == 24) {
            if (mode == 0) {
                pins.analogWritePin(AnalogPin.P7, 1023)
                pins.analogWritePin(AnalogPin.P5, 1023)
                pins.analogWritePin(AnalogPin.P6, 0)
            } else if (mode == 1) {
                pins.analogWritePin(AnalogPin.P6, 0)
            }
            P6x = 0
            SELECTED_COLOR = 1
        } else if (code == 122) {
            if (mode == 0) {
                pins.analogWritePin(AnalogPin.P6, 1023)
                pins.analogWritePin(AnalogPin.P5, 1023)
                pins.analogWritePin(AnalogPin.P7, 0)
            } else if (mode == 1) {
                pins.analogWritePin(AnalogPin.P7, 0)
            }
            P7x = 0
            SELECTED_COLOR = 2
        } else if (code == 16) {
            discoMode = true
            start = input.runningTime()
            while (input.runningTime() - start < 10000) {
                randomColorStep()
                // fast transition (change this to 100 for faster disco!)
                basic.pause(200)
            }
            // After 10 seconds, turn off LED
            pins.analogWritePin(AnalogPin.P5, 1023)
            pins.analogWritePin(AnalogPin.P6, 1023)
            pins.analogWritePin(AnalogPin.P7, 1023)
            discoMode = false
        } else if (code == 56) {
        	
        } else if (code == 90) {
        	
        } else if (code == 66) {
        	
        } else if (code == 74) {
        	
        } else if (code == 82) {
            control.reset()
        } else {
        	
        }
    }
})
