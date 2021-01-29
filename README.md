# DebouncerPIO
A PIO library to debounce input on Raspberry Pi Pico

This should trigger a callback every time a button is pressed. There are two classes: DebouncerLowPIO and DebouncerHighPIO. The former is for buttons that pull the input low and the latter is for ones that pull the input high. They're initialised with DebouncerLowPIO(statemachine, pin_number, callback). It's possible that callback will be called more than once a button press -- the debouncing isn't perfect. It can probably be optimised.

It will automatically add a pullup/down so you can just wire the button straight into the GPIO. There are also start() and stop() methods should you with to pause the state machine.

You'll need ot copy the DebouncerPIO file to your Pico, then it should work with (for example)

```
import DebouncerPIO

def handler(sm):
    print("Here")
    
button = DebouncerPIO.DebouncerLowPIO(0,0,handler)
```
