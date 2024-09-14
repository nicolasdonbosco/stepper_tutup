import RPi.GPIO as GPIO
import time

# Pin definitions
PUL_PIN = 23  # Pulse pin (BCM numbering)
DIR_PIN = 24  # Direction pin (BCM numbering)

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUL_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

# Set initial direction
GPIO.output(DIR_PIN, GPIO.HIGH)

forward = True

# Pulse function
def step_motor(steps, delay_us, fwd):
    if fwd:
        print("Forward")
        GPIO.output(DIR_PIN, GPIO.LOW)  # Toggle direction
        forward = False
    else:
        print("Backward")
        GPIO.output(DIR_PIN, GPIO.HIGH)  # Toggle direction
        forward = True
    for step in range(steps):
        GPIO.output(PUL_PIN, GPIO.HIGH)
        time.sleep(delay_us / 1_000_000.0)  # Convert microseconds to seconds
        GPIO.output(PUL_PIN, GPIO.LOW)
        time.sleep(delay_us / 1_000_000.0)

        # After 2000 steps, reverse direction


        print(step)

try:
    while True:
        step_motor(100, 600, True)  # Run for 2000 steps with a 2000us delay
        step_motor(100, 600, False)  # Run for 2000 steps with a 2000us delay
        time.sleep(0.5)

finally:
    GPIO.cleanup()  # Clean up on exit
