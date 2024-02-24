#Import necessary libraries
import mbuild,mbot2,time,event,cyberpi,random

# Global variable to control events
running = True

# When the mBot2 robot is powered on
@event.start
def start_mbot2():
    # Upon mBot2 startup, turn on rear LEDs in white
    cyberpi.led.on  (255,255,0, id = all)
    cyberpi.led.show ("w w w w w")

# Pressing button A
@event.is_press('a')
 
def button_a():
    
    global running
    running = True
    
    while running:
        # Turn on rear LEDs in green
        cyberpi.led.on  (255,255,0, id = all)
        cyberpi.led.show ("g g g g g")
        
        # Check if there's an obstacle within 10cm
        if mbuild.ultrasonic2.get(1) < 15:
        # mbot2 turn 
            # Save turn direction for LED indicators
            intermitente = random.choice([-135,-90,90,135])
            if intermitente < 0:
                cyberpi.led.show ("o o g g g")
            else:
                cyberpi.led.show ("g g g o o")
            
            mbot2.turn (intermitente)
            time.sleep(0.1)
        
        # If not, move forward at a speed of 15 and pause iteration for 0.1s
        else:
            mbot2.forward (30)

# Pressing button B
@event.is_press('b')
def button_b():
    
    global running
    running = False
    
    # LEDs in red
    cyberpi.led.on  (255,255,0, id = all)
    cyberpi.led.show ("r r r r r")
    
    # Stop mBot2
    mbot2.EM_stop('ALL')
