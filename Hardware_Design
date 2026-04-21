Dưới đây là nội dung chi tiết cho mục **Hardware Design** trên GitHub của bạn, được viết bằng tiếng Anh chuyên nghiệp để phù hợp với môi trường học thuật tại Centennial College, dựa trên tài liệu Milestone 2 của bạn:

---

## 🛠 Hardware Design

The **Smart Cat Care System** is built on a modular architecture centered around the **Raspberry Pi 4 Model B**. The design focuses on reliability, precise actuation, and safety for the pet.

### 1. System Architecture
[cite_start]The hardware is divided into three functional subsystems[cite: 8, 13]:
* [cite_start]**Identification Subsystem:** Utilizes a **PN532 RFID/NFC Module** to detect and verify unique pet IDs[cite: 17, 30].
* [cite_start]**Actuation Subsystem:** Employs a **NEMA 17 Stepper Motor** driven by a **TMC2208 Driver** for controlled food dispensing[cite: 18, 19, 57].
* [cite_start]**Monitoring Subsystem:** Uses a **JSN-SR04T Waterproof Ultrasonic Sensor** for non-contact food level tracking[cite: 20, 85].

### 2. Wiring and Interface Protocols
[cite_start]To ensure high data throughput and precise control, the following protocols are implemented[cite: 22]:

| Component | Interface | Key Pins (GPIO) | Rationale |
| :--- | :--- | :--- | :--- |
| **PN532 RFID** | **SPI** | 10 (MOSI), 9 (MISO), 11 (SCK), 8 (CE0) | [cite_start]Chosen over I2C for higher data speeds and stable tag detection[cite: 23, 24]. |
| **TMC2208 Driver** | **Step/Dir** | 17 (Step), 27 (Dir) | [cite_start]Allows for 1/16 micro-stepping to achieve near-silent operation[cite: 25, 26]. |
| **JSN-SR04T** | **Digital** | 23 (Trigger), 24 (Echo) | [cite_start]Industrial-grade sensor for accurate distance measurement in dusty environments[cite: 27, 90, 91]. |

### 3. Critical Circuit Features
* [cite_start]**Voltage Protection:** A voltage divider circuit ($1k\Omega$ and $2k\Omega$ resistors) is integrated into the Echo pin of the ultrasonic sensor to step down the 5V signal to 3.3V, protecting the Raspberry Pi’s GPIO ports[cite: 27].
* [cite_start]**StealthChop™ Technology:** By utilizing the TMC2208 driver, the system ensures the stepper motor operates quietly, preventing the pet from being startled during feeding cycles[cite: 26].
* [cite_start]**Power Management Strategy:** To prevent system "brown-outs," the project uses a dual-rail power supply[cite: 120]:
    * [cite_start]**12V DC:** Dedicated supply for the NEMA 17 motor and driver[cite: 120].
    * [cite_start]**5V/3A DC:** Dedicated logic power for the Raspberry Pi 4[cite: 120].

### 4. Technical Risks & Hardware Mitigation
* [cite_start]**Motor Jamming:** The system is designed to support a software-driven "counter-rotation" (reverse) logic to clear potential blockages in the food auger[cite: 118].
* [cite_start]**Sensor Noise:** To account for the uneven surface of the cat food, a **Moving Average Filter** is implemented in the software to smooth out ultrasonic readings[cite: 119].

---
[cite_start]*Note: This documentation is based on the technical validations performed during Milestone 2[cite: 1, 8].*
