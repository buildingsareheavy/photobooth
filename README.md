# Photobooth

A Raspberry Pi photobooth that captures photos and prints them to a thermal receipt printer.

Includes a **dev mode** so you can develop and test on your regular computer without any Pi hardware.

---

## Hardware

- Raspberry Pi 3B+
- Raspberry Pi Camera Module 2
- Raspberry Pi Touch Display 2 (800×480)
- Thermal receipt printer (USB or Ethernet, ESC/POS compatible)

---

## Requirements

- Python 3.13 (if using pyenv)
- A webcam (dev mode only)
- Linux or macOS (dev mode only)

---

## Setup

### 1. Prerequisites

**Linux**

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash
```

**macOS**

```bash
brew install pyenv
pyenv install 3.13
```

**Linux and macOS**

Add to `~/.zshrc` (or `~/.bashrc`):

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Then:

```bash
source ~/.zshrc
pyenv install 3.13
```

**Raspberry Pi**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-picamera2 python3-venv
```

---

### 2. Clone the repo

```bash
git clone https://github.com/buildingsareheavy/photobooth.git
cd photobooth
```

---

### 3. Install dependencies

**Dev machine:**

```bash
make setup
```

**Raspberry Pi:**

```bash
make setup-pi
```

---

### 4. Run

```bash
make run
```

> **dev mode:** On your dev machine the shutter is triggered by spacebar or
> mouse click. Photos are saved to `./captures/` instead of printing.

---
