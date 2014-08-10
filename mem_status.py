import RPi.GPIO as GPIO
import psutil


def main():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    while True:
        memory = psutil.virtual_memory()[2]
        if memory < 20:
            GPIO.output(16, True)
            GPIO.output(11, False)
            GPIO.output(12, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
        if 40 > memory > 20:
            GPIO.output(16, True)
            GPIO.output(11, True)
            GPIO.output(12, False)
            GPIO.output(13, False)
            GPIO.output(15, False)
        if 60 > memory > 40:
            GPIO.output(16, True)
            GPIO.output(11, True)
            GPIO.output(12, True)
            GPIO.output(13, False)
            GPIO.output(15, False)
        if 80 > memory > 60:
            GPIO.output(16, True)
            GPIO.output(11, True)
            GPIO.output(12, True)
            GPIO.output(13, True)
            GPIO.output(15, False)
        if memory > 80:
            GPIO.output(16, True)
            GPIO.output(11, True)
            GPIO.output(12, True)
            GPIO.output(13, True)
            GPIO.output(15, True)


if __name__ == '__main__':
    main()
