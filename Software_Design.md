# Software Operational Logic (Preliminary)

## 1. Multithreading Architecture
To ensure real-time responsiveness, the system runs three concurrent threads:
- **Thread_Access:** Polls RFID tags and controls the Solenoid door.
- **Thread_Feeder:** Monitors the RTC and triggers the NEMA 17 motor for scheduled meals.
- **Thread_Monitor:** Measures food levels and updates the Dual OLED displays.

## 2. Emergency Interrupt Logic
The system uses a **Hardware Interrupt** on GPIO 22. When the Emergency Button is pressed, the system immediately:
1. Halts all motor rotations.
2. Disengages the Solenoid lock (Fail-open).
3. Activates the Buzzer and flashes "EMERGENCY" on OLEDs.

## 3. Pseudo-code
```python
FUNCTION main():
    START Thread_Access()
    START Thread_Feeder()
    START Thread_Monitor()
    ENABLE Hardware_Interrupt(GPIO_22, CALLBACK=Emergency_Mode)

FUNCTION Thread_Access():
    IF RFID_Tag == AUTHORIZED:
        OPEN_DOOR()
        WAIT 10s
        CLOSE_DOOR()
