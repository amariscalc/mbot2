# 01 -  Esquivar obtáculos. POC mbot2 abs

import mbuild, mbot2, event, time, cyberpi

@event.start

# Crear la función start para comenzar el funcionamiento
def start ():
    
    # Crear un loop
    while True:
        # Comprobar mediante el ultrasonido si tenemos delante un objeto, en caso afirmativo, giramos.
        if mbuild.ultrasonic2.get (1) < 10:
            mbot2.turn (-90)
        else:
            mbot2.forward (15)
        time.sleep (0.1)
