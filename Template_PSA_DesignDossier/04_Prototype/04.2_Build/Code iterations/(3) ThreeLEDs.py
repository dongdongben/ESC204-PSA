'''
ESC204 PSA iteration three
Task: TOGGLE light up THREE external LED on button press.
All lights are present after this iteratoin
'''
# Import libraries needed for blinking the LED
import board
import digitalio
import time
# Configure the GPIO pin connected to the RED LED as a digital output
led_red = digitalio.DigitalInOut(board.GP16)
led_red.direction = digitalio.Direction.OUTPUT
#Configure the GPIO pin for BLUE LED
led_blue = digitalio.DigitalInOut(board.GP22)
led_blue.direction = digitalio.Direction.OUTPUT
#Confiture the GPIO pin for GREEN LED
led_green = digitalio.DigialInOut(board.GP3)
led_green.direction = digitalio.Direction.OUTPUT
# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor
# Print a message on the serial console
print('Hello! My LED is controlled by the button.')


led_red_state = False
led_blue_state = False
led_green_state = False
prev = button.value   #button.value = True by default (unpressed). This is an active low button

print("Button toggle script running.")

# --- Main loop ---
while True:   #keep looping to poll the button state
    # Always call button.update() in the loop to check the button's state
    curr = button.value   #check current button state 
    if prev and not curr:    #check if state changes
        led_red_state = not led_red_state
        led_blue_state = not led_blue_state
        led_green_state = not led_green_state
        
        led_red.value = led_red_state    #if button state changes (pressed), update the led state
        led_blue.value = led_blue_state
        led_green.value = led_green_state
        print(f"LED state changed to: {led_blue_state}")
    prev = curr
    time.sleep(0.01)



