# DebouncerPIO
A PIO library to debounce input on Raspberry Pi Pico

Not sure if this is a good use of PIO, but it is A use of PIO. Currently only debounces signals that pull low, but a simple change to add pull high signals in there as well. Just need to flip some 0s to 1s. I'll do it if people find it useful.

The timings may need tweaking, and it could probably be made much more robust.

You'll need ot copy the DebouncerPIO file to your Pico, then it should work with (for example)

```
import DebouncerPIO

def handler(sm):
    print("Here")
    
button = DebouncerPIO.DebouncerLowPIO(0,0,handler)
```
