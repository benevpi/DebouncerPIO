from machine import Pin
import rp2
import time

@rp2.asm_pio()
def debounce_low():
    wait(0, pin, 0)
    set(y,7)
    label("loop")
    nop() [10]
    jmp(y_dec, "loop")
    in_(pins,1)
    mov(isr, y)
    jmp(y, "skip")
    irq(block, rel(0))
    wait(1, pin, 0)
    label("skip")
    
class DebouncerLowPIO:
    
    def __init__(self, statemachine, pin_number, handler):
        self.pin = Pin(0, Pin.IN, Pin.PULL_UP)
        self.sm  = rp2.StateMachine(0, debounce_low, in_base=self.pin, freq=2000)
        self.sm.irq(handler)
        self.sm.active(1)
        
    def stop(self):
        self.sm.active(0)
        
    def start(self):
        self.sm.active(1)