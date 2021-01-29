import DebouncerPIO

def handler(sm):
    print("Here low")
    
def handler_high(sm):
    print("Here high")
    
button = DebouncerPIO.DebouncerLowPIO(0,0,handler)

button2 = DebouncerPIO.DebouncerHighPIO(1,1,handler_high)