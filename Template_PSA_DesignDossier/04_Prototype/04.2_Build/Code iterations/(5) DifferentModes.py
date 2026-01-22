'''
ESC204 PSA iteration Final
Now allows the control of all modes (all off, 2 on, 3on) with
one button. More details of the modes are int the RFP
'''
# Import libraries needed for blinking the LED
import board
import digitalio
import time
# Configure the GPIO pin connected to the RED LED as a digital output
led_red = digitalio.DigitalInOut(board.GP26)
led_red.direction = digitalio.Direction.OUTPUT
#Configure the GPIO pin for BLUE LED
led_blue = digitalio.DigitalInOut(board.GP28)
led_blue.direction = digitalio.Direction.OUTPUT
#Confiture the GPIO pin for GREEN LED
led_green = digitalio.DigitalInOut(board.GP3)
led_green.direction = digitalio.Direction.OUTPUT
# Configure the GPIO pin connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Set internal pull-up resistor
# Print a message on the serial console
print('Hello! My LED is controlled by the button.')

#define the 3 different modes for: completely off, plants only LED, and plants and people LED
def Mode1():
    led_red.value = False
    led_blue.value = False
    led_green.value = False
def Mode2():
    led_red.value = True
    led_blue.value = True
    led_green.value = False
def Mode3():
    led_red.value = True
    led_blue.value = True
    led_green.value = True

#Construct a list that holds these states
modes = [Mode1, Mode2, Mode3]
mode_i = 0
modes[mode_i]()  # apply initial state


prev = button.value   #button.value = True by default (unpressed). This is an active low button

print("Button toggle script running.")

# --- Main loop ---
while True:   #keep looping to poll the button state
    # Always call button.update() in the loop to check the button's state
    curr = button.value   #check current button state 
    if prev and not curr:    #check if button state changes (aka is pressed)
        #increment the mode number if so
        mode_i = (mode_i+1) % len(modes)
        #call the mode function to change LED lighting
        modes[mode_i]()
        print(f"changed to Mode {mode_i + 1}")
    prev = curr
    time.sleep(0.01)







