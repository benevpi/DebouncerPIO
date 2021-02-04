from machine import Pin
import rp2
import time

@rp2.asm_pio()
def debounce_low():
    wait(0, pin, 0)
    
    set(y,7)
    label("loop")
    jmp(y_dec, "loop") [10]
    in_(pins,1) 
    mov(isr, y)
    jmp(y, "skip")
    
    set(y,7)
    label("loop2")
    jmp(y_dec, "loop2") [10]
    in_(pins,1) 
    mov(isr, y)
    jmp(y, "skip")
    
    set(y,7)
    label("loop3")
    jmp(y_dec, "loop3") [10]
    in_(pins,1) 
    mov(isr, y)
    jmp(y, "skip")
    
    irq(block, rel(0))
    wait(1, pin, 0)
    label("skip") #no idea why this isn't triggering the not-wrapping bug that debounce-high is
    
@rp2.asm_pio()
def debounce_high():
    wait(1, pin, 0)
    
    set(y,7)
    
    label("loophigh")
    jmp(y_dec, "loophigh") [10]
    
    in_(pins,1)
    mov(y, isr)
    jmp(not_y, "skiphigh")
    
    set(y,7)
    
    label("loophigh2")
    jmp(y_dec, "loophigh2") [10]
    
    in_(pins,1)
    mov(y, isr)
    jmp(not_y, "skiphigh")
    
    #and once more
    
    
    irq(block, rel(0))
    
    wait(0, pin, 0)
    label("skiphigh")
    set(y,1) # just a test -- doesn't work if removed. looks like it's not wrapping

class DebouncerLowPIO:
    
    def __init__(self, statemachine, pin_number, handler):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self.sm  = rp2.StateMachine(statemachine, debounce_low, in_base=self.pin, freq=2000)
        self.sm.irq(handler)
        self.sm.active(1)
        
    def stop(self):
        self.sm.active(0)
        
    def start(self):
        self.sm.active(1)
        
class DebouncerHighPIO:
    
    def __init__(self, statemachine, pin_number, handler):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_DOWN)
        self.sm  = rp2.StateMachine(statemachine, debounce_high, in_base=self.pin, freq=3000)
        self.sm.irq(handler)
        self.sm.active(1)
        
    def stop(self):
        self.sm.active(0)
        
    def start(self):
        self.sm.active(1)