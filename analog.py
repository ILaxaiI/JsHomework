import time
import explorerhat
import RPi.GPIO as GPIO
import math
## These lines configure the PWM pin for pulse width modulation
## You don't need to make any changes to these lines
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 400)


#####################################
## Here we define some parameters
# the minimum and maximum frequency our buzzer should use as well as the duration of the buzzer sound
minfreq = 100
maxfreq = 800
buzzdur = 0.25

# the value range we expect from our trim resistor
minvolt = 0
maxvolt = 5.2

# our sampling mode is either time continuous or time discrete
mode = "timeCont"   #allowed values are "timeCont" for time continous or "timeDisc" for time discrete sampling
samplingfreq = 60   #for mode "timeDisc" the sampling frequency is used

# here we set, how many bits our A/D converter should employ
bits = 1
#####################################



#####################################
### no changes needed in this section

## as a helper function, we copied our decToBin function from a former exercise
## it converts a decimal number between 0 and 15 into a four bit array
def decToBin(decimal, bits):
    tmp = decimal
    binArray = [0] * bits
    for i in reversed(range(0, bits)):
        binArray[i] = decimal%2
        decimal = decimal//2
    print("{} as binary is {}".format(tmp,binArray[::-1]))
    return binArray

## as a helper function, binToDec transforms a binary representation
## of a number into a decimal representation
def binToDec(binArray):
    binArray = binArray[::-1]
    result = 0
    for i in range(0, len(binArray)):
        result = result + binArray[i]*(2**i)
    print("{} as decimal is {}".format(binArray[::-1], result))
    return result

    
## A little helper function to trigger the buzzer. We pass the frequency as well
## as the buzzer duration
def buzz(freq, dur):
    buzzer.ChangeFrequency(freq)
    buzzer.start(10)
    time.sleep(dur)
    buzzer.stop()
#####################################
    
    
    

def mapValue(value):
   return (value < minvolt and minfreq) or (value> maxvolt and maxfreq) or minfreq+(maxfreq-minfreq)*value/maxvolt


## the 1 Bit A/D converter
## it should return either a [0] or [1]
def AD1Bit(value):
    result = [0]
    if value > 5.2/2:
        result[0] = 1
    toggleLED(result)
    toggleBuzz(result)
    return result




## the 2 Bit A/D converter
def AD2Bit(value):
    result = [0, 0]

    if value > 3.9:
       result[0] = 1
       result[1] = 1
    elif value > 2.6:
        result[0] = 1
    elif value > 1.3:
        result[1] = 1
        

    toggleLED(result)
    toggleBuzz(result)
    return result


## the n Bit A/D uses between 1 and 4 bit for conversion
def ADnBit(value, bit):
    if bit > 4 or bit < 1:
        print("Invalid number of bits")
        return
    
    decRes = math.floor(value/5.2*(2**bit-1))
    result = decToBin(decRes,bit)

    
    toggleLED(result)
    toggleBuzz(result)
    return result



## Here we toggle the LEDs according to our digitized voltage value
def toggleLED(quantValue):
    if len(quantValue) > 4:
        print("You try to address too many LEDs")
    for lamp in range(0,4):
        if lamp < len(quantValue) and quantValue[lamp]:
            explorerhat.output[lamp].on()
        else:
            explorerhat.output[lamp].off()
        

## toggleBuzz invokes the buzzer with a frequency corresponding to the quantized value
def toggleBuzz(quantValue):
    buzzfreq = 400
    #...
    buzz(buzzfreq, buzzdur)
    

    

## Here we set the explorer hat buttons to select who many bits our A/D converter should employ
def evaluateButtons(channel, event):
    global bits
    if event =="press" and channel <5:
        bits = channel
    # ...

## We register the handler evaluteButtons for button press events
explorerhat.touch.pressed(evaluateButtons)




while 1:
    ## here we read the current voltage value from our analog pin
    currentValue = explorerhat.analog.one.read()
    print("Reading value {}".format(currentValue))
    
    ## here we invoke mapValue in order to directly map a voltage value to a frequency
    ## we then call the buzz function with the resulting frequency in order to "hear" our
    ## value. Try then changing the trimmer setting with a screwdriver while running this code
    ## For the following tasks, you need to comment these two lines out
    resultingFreq = mapValue(currentValue)
    buzz(resultingFreq, buzzdur)
    
    ## here we trigger the A/D conversion either for 1 or more Bits
    ## please comment the two lines of code above (resultingFreq =..., buzz...) out
    #result = AD1Bit(currentValue)
    #result = AD2Bit(currentValue)
    result = ADnBit(currentValue, bits)
    
    ## When invoking the A/D conversion you may uncomment this print call
    print("Mapping {} to {} by using {}-bit A/D conversion.".format(currentValue, result, len(result)))    
    
    ## in case we use time discrete mode, we use the sampling frequency defined above
    if mode == "timeDisc":
        time.sleep(60/samplingfreq)   
        
    

