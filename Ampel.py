import time
import explorerhat
#Eine Hilfsfunktion, die uns unsere Zustandsnamen auf Codierungen abbildet
#Hier ist nichts zu verändern, es sei denn, Sie verwenden eine andere
#Kodierung

#Der initiale Zustand: Die Ampel ist auf rot
state = "rot"

#Die Zeit, die zwischen Umschaltvorgängen vergeht
waitingtime =3

#Anforderungskontakt gedrückt oder nicht
pedestrian_req = 0

#der Handler, um einen Druck auf die Anforderungstaste entgegenzunehmen
def pedreq(channel, event):
    global pedestrian_req
    pedestrian_req = 1

    #wenn Taste 1 gedrückt, setzen wir pedestrian_req

#ampel schaltung simuliert durch logische ausdrücke

def rot(a,b):
    return not a
def gelb(a,b):
    return b == 1
def gruen(a,b):
    return not (not a or b)


ampel = {
    "rot":rot,
    "gelb":gelb,
    "gruen":gruen
}

#Registrierung des Handlers, der die Fußgängeranforderung entgegennimmt
explorerhat.touch.pressed(pedreq)

out = [0,0]
while 1:
   
    #zu Beginn jedes Durchlaufs wird der aktuelle Zustand nach
    #außen gegeben. Da output.on() bewirkt, dass der Pin auf
    #GND (also die logische 0) gezogen wird, invertieren wir
    #das jeweilige Bit der Zustandskodierung
    #Hier sollten Sie nichts verändern

    explorerhat.output[1].write(not out[0])
    explorerhat.output[0].write(not out[1])
    
    #Die eigentliche Zustandsmaschine, die basierend auf aktuellem Zustand
    #und optionalem Eingang entscheidet, was der Folgezustand sein wird

    
    if state == "rot":
        #für Ihre Fehlersuche ggf. hilfreich
        out[1] = 0
        out[0] = 0 
        #Onboard LEDs des Explorer HAT ein- und ausschalten
    
        explorerhat.light.red.on()
        explorerhat.light.yellow.off()
        explorerhat.light.green.off()
        
        #Hier prüfen wir die Fußgägngeranforderung und schalten
        #die Fußgängerampel ggf. auf grün (blau)
        #if ...
        if pedestrian_req:
            pedestrian_req = 0

            explorerhat.light.blue.on()
            #blau on
        #durch welche Zuweisung wechseln Sie in den nächsten Zustand?
        #state = ...   

        state = "gelb"
    elif state == "gelb":
        #blau off
        
        state = (out[0] and "rot" or "gruen")
        
        explorerhat.light.blue.off()
        explorerhat.light.yellow.on()
        explorerhat.light.green.off()
        out[1] = 1

    elif state == "gruen":
        out[0] = 1
        out[1] = 0
        state = "gelb"

        explorerhat.light.red.off()
        explorerhat.light.yellow.off()
        explorerhat.light.green.on()

    print(out)
    print(ampel["rot"](out[0],out[1]),ampel["gelb"](out[0],out[1]),ampel["gruen"](out[0],out[1]),)
    #sleep for nächstem state
    time.sleep(waitingtime)
    
time.sleep(5)
