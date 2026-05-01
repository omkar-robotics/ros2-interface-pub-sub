# ROS2 Interface Publisher-Subscriber System

## 📌 Overview

This project demonstrates a ROS 2-based communication system using a custom message interface. It implements a publisher-subscriber architecture to simulate real-time hardware monitoring (temperature, motor status, debug info).

---

## 🚀 Features

* Custom ROS2 interface (`HardwareStatus.msg`)
* Publisher node simulating hardware data
* Subscriber node for monitoring system state
* Real-time communication using ROS2 topics
* Clean modular architecture (separate interface + nodes)

---

## 🏗️ Architecture

```
HardwarePublisher Node
        │
        ▼
   /hardware_status  (Topic)
        │
        ▼
HardwareSubscriber Node

        ↑
 HardwareStatus.msg (Interface)
```

---

## 📦 Project Structure

```
interface_ws/
├── src/
│   ├── my_robot_interfaces/
│   │   ├── msg/
│   │   │   └── HardwareStatus.msg
│   │   ├── package.xml
│   │   └── CMakeLists.txt
│   │
│   ├── my_py_pkg/
│   │   ├── my_py_pkg/
│   │   │   ├── hardware_publisher.py
│   │   │   ├── hardware_subscriber.py
│   │   │   └── __init__.py
│   │   ├── package.xml
│   │   ├── setup.py
│   │   └── setup.cfg
│
└── README.md
```

---

## 🧠 Custom Message Definition

File: `HardwareStatus.msg`

```
int64 version
float64 temperature
bool are_motors_ready
string debug_message
```

---

## ⚙️ Setup & Installation

```bash
# Create workspace
mkdir -p ~/interface_ws/src
cd ~/interface_ws/src

# Clone repository
git clone https://github.com/omkar-robotics/ros2-interface-pub-sub.git

# Build workspace
cd ~/interface_ws
colcon build

# Source workspace
source install/setup.bash
```

---

## ▶️ Usage

### Run Subscriber (Terminal 1)

```bash
ros2 run my_py_pkg hardware_sub
```

### Run Publisher (Terminal 2)

```bash
ros2 run my_py_pkg hardware_pub
```

---

## 📊 Sample Output

```
Publishing:
Version: 1
Temperature: 45.3
Motors Ready: True

Received:
Version: 1, Temp: 45.3, Motors: True

High Temperature: 65.0
Motors NOT ready!
```

---

## 🧩 Technologies Used

* ROS 2 (Humble)
* Python (rclpy)
* Custom Interfaces (.msg)
* Colcon Build System

---

## 📷 Output Preview

<img width="100%" src="Screenshot from 2026-05-01 12-33-08.png" />

---

## 📈 Future Improvements

* Integration with real sensors (camera, temperature)
* ROS2 bag recording for data logging
* Visualization using RViz
* Gazebo simulation integration
* Add service & action interfaces

---

## 👨‍💻 Author

Omkar
GitHub: https://github.com/omkar-robotics

---
