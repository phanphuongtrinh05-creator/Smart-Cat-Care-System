import threading

# Thêm Lock để bảo vệ biến shared
emergency_lock = threading.Lock()
is_emergency = False

def emergency_callback(channel):
    global is_emergency
    with emergency_lock:
        is_emergency = True
    print("!!! EMERGENCY PRESSED !!!")
    GPIO.output(PIN_SOLENOID, GPIO.HIGH)
    GPIO.output(PIN_BUZZER, GPIO.HIGH)

def emergency_callback(channel):
    global is_emergency
    with emergency_lock:
        is_emergency = True
    print("!!! EMERGENCY PRESSED !!!")
    GPIO.output(PIN_SOLENOID, GPIO.HIGH)
    GPIO.output(PIN_BUZZER, GPIO.HIGH)
    time.sleep(2)  # Hú 2 giây
    GPIO.output(PIN_BUZZER, GPIO.LOW)  # Tắt còi
    # Dừng các luồng khác nếu cần

GPIO.add_event_detect(PIN_EMERGENCY_BUTTON, GPIO.FALLING, 
                       callback=emergency_callback, bouncetime=300)

def thread_access_control():
    print("RFID Thread Started...")
    while not is_emergency:
        # tag_id = rfid.read() 
        time.sleep(1) 
        # Nếu quét đúng thẻ:
        # GPIO.output(PIN_SOLENOID, GPIO.HIGH)
        # time.sleep(10)
        # GPIO.output(PIN_SOLENOID, GPIO.LOW)

def thread_feeder_schedule():
    print("Feeder Thread Started...")
    last_feed_time = None
    
    while not is_emergency:
        current_time = time.strftime("%H:%M")
        
        # Chỉ cho ăn 1 lần mỗi khung giờ
        if (current_time == "07:00" or current_time == "18:00") and \
           current_time != last_feed_time:
            print(f"Time to eat at {current_time}! Dispensing food...")
            
            GPIO.output(PIN_MOTOR_DIR, GPIO.HIGH)
            for _ in range(2000):
                if is_emergency:  # Dừng ngay nếu có emergency
                    break
                GPIO.output(PIN_MOTOR_STEP, GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(PIN_MOTOR_STEP, GPIO.LOW)
                time.sleep(0.001)
            
            last_feed_time = current_time
        
        time.sleep(30)  # Kiểm tra mỗi 30 giây thay vì 1 giây

# --- 4. LUỒNG GIÁM SÁT & HIỂN THỊ (Monitoring Thread) ---
def thread_monitoring():
    global food_level
    print("Monitoring Thread Started...")
    
    while not is_emergency:
        # Giả lập đọc cảm biến
        # food_level = calculate_percentage(sensor.get_distance())
        
        if food_level < 10:
            print(f"Warning: Low Food! ({food_level}%)")
            # Buzzer beep pattern
            for _ in range(3):
                if is_emergency:
                    break
                GPIO.output(PIN_BUZZER, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(PIN_BUZZER, GPIO.LOW)
                time.sleep(0.2)
        
        time.sleep(5)

# --- CHƯƠNG TRÌNH CHÍNH ---
if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=thread_access_control, daemon=True)
        t2 = threading.Thread(target=thread_feeder_schedule, daemon=True)
        t3 = threading.Thread(target=thread_monitoring, daemon=True)

        t1.start()
        t2.start()
        t3.start()

        print("System running... Press Ctrl+C to stop")
        
        while not is_emergency:
            time.sleep(1)
        
        if is_emergency:
            print("Emergency mode activated - system halted")
            while True:  # Giữ emergency state
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nSystem Shutdown Requested")
    finally:
        print("Cleaning up GPIO...")
        GPIO.cleanup()


PIN_RESET_BUTTON = 23  # Nút reset

GPIO.setup(PIN_RESET_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def reset_callback(channel):
    global is_emergency
    with emergency_lock:
        if is_emergency:
            is_emergency = False
            GPIO.output(PIN_SOLENOID, GPIO.LOW)
            GPIO.output(PIN_BUZZER, GPIO.LOW)
            print("Emergency reset - system resuming")

GPIO.add_event_detect(PIN_RESET_BUTTON, GPIO.FALLING,
                      callback=reset_callback, bouncetime=300)
