'''
ESC204 PSA iteration one
Task: TOGGLE light up external LED on button press.
Solves the first demand of toggling LED
'''
# Import libraries needed for blinking the LED
import board
import digitalio
import time
# Configure the GPIO pin connected to the LED as a digital output
led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT
# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor
# Print a message on the serial console
print('Hello! My LED is controlled by the button.')


led_state = False
prev = button.value   #button.value = False by default (unpressed). This is an active low button

print("Button toggle script running.")

# --- Main loop ---
while True:   #keep looping to poll the button state
    # Always call button.update() in the loop to check the button's state
    curr = button.value   #check current button state 
    if prev and not curr:    #check if state changes
        led_state = not led_state
        led.value = led_state    #if button state changes (pressed), update the led state
        print(f"LED state changed to: {led_state}")
    prev = curr
    time.sleep(0.01)

