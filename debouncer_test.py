import DebouncerPIO

def handler(sm):
    print("Here")
    
button = DebouncerPIO.DebouncerLowPIO(0,0,handler)