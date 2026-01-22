'''
ESC204 PSA iteration two
Task: TOGGLE light up TWO external LED on button press.
Heading towards the requirements
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
# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor
# Print a message on the serial console
print('Hello! My LED is controlled by the button.')


led_red_state = False
led_blue_state = False
prev = button.value   #button.value = True by default (unpressed). This is an active low button

print("Button toggle script running.")

# --- Main loop ---
while True:   #keep looping to poll the button state
    # Always call button.update() in the loop to check the button's state
    curr = button.value   #check current button state 
    if prev and not curr:    #check if state changes
        led_red_state = not led_red_state
        led_blue_state = not led_blue_state
        led_red.value = led_red_state    #if button state changes (pressed), update the led state
        led_blue.value = led_blue_state
        print(f"LED state changed to: {led_blue_state}")
    prev = curr
    time.sleep(0.01)


