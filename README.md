# Remote-keylogger
remote key logger is used to store every single key stroke of the compromised system. further, it sends the recorded keystrokes to the the attacker's system.
# Remote Keylogger Proof-of-Concept

> **Disclaimer**: This project is created strictly for **educational** and **research** purposes. Unauthorized use of keyloggers is illegal and unethical. Use this only on systems you **own** or have **explicit permission** to test.

## Overview

This project demonstrates a basic **remote keylogger** written in Python. It includes:

- A **server script** that runs on the attacker's machine and logs keystrokes.
- A **client script** that runs on the victim's machine and captures keystrokes.
- A sample output file (`logged.txt`) showing logged keystrokes.

## 🗂 Project Structure
├── client.py # Runs on attacker's machine
├── server.py # Runs on victim's machine
├── logged.txt # Example keystroke log
└── README.md # Project documentation

## ⚙️ Prerequisites

- Python 3.6+
- Install `pynput` for keylogging:

```bash
pip install pynput
```


To stop keylogging on the victim's machine, press the Esc key.


