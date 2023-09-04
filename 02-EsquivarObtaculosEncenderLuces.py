# 02 -  Esquivar obtáculos. Detener. Encender luces cyberpi
import mbuild, mbot2, event, time, cyberpi, random


@event.is_press ('a')
def button_a_is_pressed():
    
    # Activar los 5 led del cyberpi y asignar colores (g = green, w = white)
    cyberpi.led.on  (255,255,0, id = all)
    cyberpi.led.show ("g w g w g")
    # Comprobar mediante el ultrasonido si tenemos delante un objeto, en caso afirmativo, giramos.
    if mbuild.ultrasonic2.get (1) < 10:
        mbot2.turn (random.choice([-135,-90,90,135]))
    else:
    # Recorrer a una velecidad de 15
        mbot2.forward (15)
    # Tiempo de espera, esto provocará que el check del ultrasonido no se ejecute continuamente.
        time.sleep (0.1)

@event.is_press ('b')
def button_b_is_pressed():
    while True:
    #Stop the mbot2
        mbot2.EM_stop ()
