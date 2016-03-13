import RPi.GPIO as GPIO

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Select all non-special GPIOs
gpios = [4, 5, 6, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

# Disable warning messages
GPIO.setwarnings(False)

print "Settings all GPIOs as input."

# Set them all as input
GPIO.setup(gpios, GPIO.IN)

print "Clean up complete."
