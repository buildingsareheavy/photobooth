# Photobooth

A Raspberry Pi photobooth that captures photos and prints them to a thermal receipt printer.

Includes a **mock mode** so you can develop and test on your regular computer without any Pi hardware.

---

## Hardware

- Raspberry Pi 3B+
- Raspberry Pi Camera Module 2
- Raspberry Pi Touch Display 2 (800×480)
- Thermal receipt printer (USB or Ethernet, ESC/POS compatible)

---

## Requirements

- Python 3.13
- A webcam (for mock mode on your dev machine)

---

## Dev Setup (mock mode)

Mock mode runs on your regular computer using a webcam. The shutter is triggered by spacebar or mouse click, and photos are saved to `./captures/` instead of printing.
