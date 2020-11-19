import board
import neopixel
import signal
import sys
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set pin 7(GPIO 4) as button
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW)    # Set pin 13(GPIO 27) to be output for LED
pixels = neopixel.NeoPixel(board.D18, 12)    #Set pin 18 as the PWM pin for NeoPixels

#Create a variable for the current button count
BUTTON_CURRENT = 0

#Define a signal handler for <CTRL> + C to exit the code
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

#Define the button press callback event
def button_pressed_callback(channel):
    print("Button pressed!")
    global BUTTON_CURRENT
    if BUTTON_CURRENT < 4:
        BUTTON_CURRENT = BUTTON_CURRENT + 1
    else:
        BUTTON_CURRENT = 0
    print (BUTTON_CURRENT)

#Determine if the button LED should be lit
    if BUTTON_CURRENT > 0:
        GPIO.output(27, GPIO.HIGH)
    else:
        GPIO.output(27, GPIO.LOW)
#Perform the function of the button selection
    if BUTTON_CURRENT == 1: # Make all LEDs Red
        pixels.fill((255, 0, 0))
    elif BUTTON_CURRENT == 2: # Make all LEDs Green
        pixels.fill((0, 255, 0))
    elif BUTTON_CURRENT == 3: # Make all LEDs Blue
        pixels.fill((0, 0, 255))
    elif BUTTON_CURRENT == 4: # Make all LEDs Purple
        pixels.fill((180, 0, 210))
    else: # Turn all LEDs off
        pixels.fill((0, 0, 0))

#Event to detect the falling edge of the button press
GPIO.add_event_detect(4, GPIO.FALLING, callback=button_pressed_callback, bouncetime=100)

#Signal handler callout for program termination
signal.signal(signal.SIGINT, signal_handler)
signal.pause()

