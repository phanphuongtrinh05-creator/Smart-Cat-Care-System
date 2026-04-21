import RPi.GPIO as GPIO
import time
import board
import busio
from adafruit_pn532.i2c import PN532_I2C
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

AUTHORIZED_UIDS = [
    [0x61, 0xf5, 0x3, 0x7],
]

def init_rfid():
    i2c = busio.I2C(board.SCL, board.SDA)
    pn532 = PN532_I2C(i2c, debug=False)
    pn532.SAM_configuration()
    print("RFID ready.")
    return pn532

def set_angle(angle):
    duty = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)

def dispense_food():
    print("Opening gate...")
    set_angle(90)
    time.sleep(1.5)
    print("Closing gate...")
    set_angle(0)
    print("Dispensing complete.")
    time.sleep(3)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    timeout = time.time() + 1
    while GPIO.input(ECHO) == 0:
        start = time.time()
        if time.time() > timeout:
            return -1
    timeout = time.time() + 1
    while GPIO.input(ECHO) == 1:
        end = time.time()
        if time.time() > timeout:
            return -1
    return (end - start) * 17150

def filtered_distance(samples=5):
    readings = [get_distance() for _ in range(samples)]
    readings = [r for r in readings if r > 0]
    if not readings:
        return -1
    return sum(readings) / len(readings)

def check_food_level():
    dist = filtered_distance()
    if dist < 0:
        print("Sensor error - check wiring.")
        return
    print(f"Food level distance: {dist:.2f} cm")
    if dist > 20:
        print("WARNING: Food level LOW! Please refill.")
    else:
        print("Food level OK.")

def main():
    pn532 = init_rfid()
    print("Smart Cat Care System running...")
    print("Waiting for RFID tag...")
    while True:
        try:
            uid = pn532.read_passive_target(timeout=0.5)
            if uid is not None:
                uid_list = list(uid)
                print(f"Tag detected: {[hex(i) for i in uid_list]}")
                if uid_list in AUTHORIZED_UIDS:
                    print("Authorized! Dispensing food...")
                    dispense_food()
                    check_food_level()
                    print("Waiting for next tag...")
                else:
                    print("Unauthorized tag.")
        except Exception as e:
            print(f"Error: {e}")
            print("Reconnecting RFID...")
            time.sleep(1)
            try:
                pn532 = init_rfid()
                print("Reconnected!")
            except Exception as e2:
                print(f"Reconnect failed: {e2}")
                time.sleep(2)
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        pwm.stop()
        GPIO.cleanup()
        print("Cleanup done.")
