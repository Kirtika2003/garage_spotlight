import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# doing this first, since we're using a while True.
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
TRIG = 4
ECHO = 18

GREEN = 17
YELLOW = 27
RED = 22

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)


def green_light():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

def yellow_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)

def red_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)


def get_distance():


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distance = sig_time / 0.000058

    #inches:
    #distance = sig_time / 0.000148
    #print('Distance: {} centimeters'.format(distance))

    return distance


while True:
    distance = get_distance()
    time.sleep(0.05)
    print(distance)

    if distance >= 30:
        green_light()
    elif 30 > distance > 10:
        yellow_light()
    elif distance <= 10:
        red_light()
