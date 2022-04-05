import aud
import bpy
from bpy.app.handlers import persistent

device = aud.Device()
sound = aud.Sound('')

def coinSound():
    handle = device.play(
                        sound
                        .triangle(1000)
                        .highpass(20)
                        .lowpass(2000)
                        .ADSR(0,0.5,1,0)
                        .fadeout(0.1,0.1)
                        .limit(0,1)
                        #.delay(1)
                        #.pitch(0.5)
                        #.volume(1)
                        )

    handle = device.play(
                        sound
                        .triangle(1500)
                        .highpass(20)
                        .lowpass(2000)
                        .ADSR(0,0.5,1,0)
                        .fadeout(0.2,0.2)
                        .delay(0.1)
                        .limit(0,1)
                        #.pitch(0.5)
                        #.volume(1)
                        )
                                        
@persistent
def playSound(dummy):
    coinSound()
    
bpy.app.handlers.render_complete.append(playSound)