# Testing and Validation Plan (Preliminary)

## 1. Unit Testing
- **RFID Test:** Verify if the system recognizes authorized vs unauthorized UIDs.
- **Motor Test:** Ensure NEMA 17 rotates the exact number of steps for 50g of food.
- **Sensor Test:** Calibrate JSN-SR04T to ensure +/- 1cm accuracy.

## 2. Integration Testing
- **Feeding & Display:** Confirm OLED updates food percentage immediately after dispensing.
- **Access & Lock:** Verify Solenoid retracts only when an authorized tag is within 3cm.

## 3. Safety Testing
- **E-Stop Test:** Verify that the Emergency Button overrides all other processes.
- **Power Fail Test:** Ensure UPS Shield keeps the Raspberry Pi running for at least 30 minutes without AC power.
