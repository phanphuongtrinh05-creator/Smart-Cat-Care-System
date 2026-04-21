

## 📝 Lab Notes & Development Journal

This section documents the technical progress and research conducted during the development of the **Smart Cat Care System**.

### Phase 1: Research & Component Selection
* [cite_start]**Component Analysis:** Conducted a comprehensive review of hardware datasheets for the **PN532** and **TMC2208**[cite: 131].
* [cite_start]**Compatibility Check:** Verified voltage compatibility between the Raspberry Pi’s 3.3V logic and the sensors' 5V requirements[cite: 131].
* **Protocol Selection:** Evaluated SPI vs. I2C for the RFID module; [cite_start]SPI was selected for its higher data throughput to ensure rapid tag detection[cite: 24, 133].

### Phase 2: Environment Setup
* [cite_start]**OS Configuration:** Initialized the **Raspberry Pi 4** with Raspbian OS[cite: 132].
* [cite_start]**Interface Enabling:** Configured the Pi to enable **SPI** and **I2C** communication via `raspi-config`[cite: 132].
* [cite_start]**Dependency Management:** Installed essential Python libraries including `spidev`, `RPi.GPIO`, `busio`, and `adafruit-circuitpython-pn532`[cite: 123, 132].

### Phase 3: System Design & Prototyping
* [cite_start]**Wiring Schematics:** Drafted the initial wiring diagrams for the TMC2208 motor driver and the ultrasonic sensor[cite: 134].
* [cite_start]**Signal Conditioning:** Designed and implemented a **voltage divider** ($1k\Omega$ and $2k\Omega$) on the Echo pin of the JSN-SR04T to protect the Pi's GPIO from 5V signals[cite: 27].
* [cite_start]**Strategy Documentation:** Defined the functional testing strategy for the "Read-then-Spin" loop[cite: 134].

### Phase 4: Validation & Testing (Milestone 2)
* [cite_start]**RFID Testing:** Successfully extracted and validated the **Unique Identifier (UID)** from RFID tags through the SPI bus[cite: 31, 112].
* [cite_start]**Actuation Testing:** Confirmed precise control of the **NEMA 17** motor rotation using the TMC2208 driver[cite: 57, 114].
* [cite_start]**Noise Mitigation:** Identified sensor noise due to uneven food surfaces and developed a **Moving Average Filter** in Python to stabilize distance readings[cite: 87, 119].

---

### Current Status (as of April 20, 2026)
* [cite_start]**Status:** Hardware wiring is finalized, and core software integration for the basic dispensing loop is complete[cite: 124].
* [cite_start]**Next Goal:** Calibration of dispensing volume (grams per step) and integration of the OLED display[cite: 128, 129].
