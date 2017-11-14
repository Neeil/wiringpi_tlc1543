import wiringpi as wp
import time


Clock = 27
Address = 28
DataOut = 29
CS = 30
EOC =26


def ADC_Read(channel):
    wp.digitalWrite(CS, 0)
    
#    if wp.digitalRead(EOC) != 1:
#        return -1

    print(wp.digitalRead(EOC))
    value = 0
    for i in range(0,4):
        if((channel >> (3-i)) & 0x01):
            wp.digitalWrite(Address, 1)
        else:
            wp.digitalWrite(Address, 0)
        wp.digitalWrite(Clock, 1)
        wp.digitalWrite(Clock, 0)
    for i in range(0, 6):
        wp.digitalWrite(Clock, 1)
        wp.digitalWrite(Clock, 0)
    wp.digitalWrite(CS, 1)
    time.sleep(0.001)
    
#    if wp.digitalRead(EOC) != 1 : 
#        return -1
 
#    print(wp.digitalRead(EOC))
#    while (wp.digitalRead(EOC) == 0):
#        print(wp.digitalRead(EOC))
#        time.sleep(0.001)

    print(wp.digitalRead(EOC))
    wp.digitalWrite(CS, 0)
    for i in range(0, 10):
        wp.digitalWrite(Clock, 1)
        value <<= 1
        if (wp.digitalRead(DataOut)):
            value |= 0x01
        wp.digitalWrite(Clock, 0)
    wp.digitalWrite(CS, 1)

    return value

wp.wiringPiSetup()


wp.pinMode(Clock,   1)
wp.pinMode(Address, 1)
wp.pinMode(DataOut, 0)
wp.pinMode(CS,  1)
wp.pinMode(EOC, 0)
try:
    while True:
        print ('AD Value: %d' %ADC_Read(1))
        time.sleep(1)
except:
    GPIO.cleanup()
