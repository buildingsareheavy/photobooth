# Photobooth

A Raspberry Pi photobooth that captures photos and prints them on an ESC/POS-compatible thermal receipt printer.

Includes a **development mode** that runs on Linux or macOS using a standard webcam. Captured images are saved to disk instead of being printed.

---

## Hardware

- Raspberry Pi 3B+ (running Raspberry Pi OS)
- Raspberry Pi Camera Module 2
- Raspberry Pi Touch Display 2 (800×480)
- Thermal receipt printer (USB or Ethernet, ESC/POS compatible)

---

## Requirements

- Python 3.10–3.13 (recommended)
- A webcam (development mode only)
- Linux or macOS (development mode only)

If you don't have a compatible Python version installed, see the **Installing Python with pyenv** section below.

Check your Python version to confirm:

```bash
python3 --version
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/buildingsareheavy/photobooth.git
cd photobooth
```

---

### 2. Install dependencies

**Linux or macOS**

```bash
make setup
```

Creates a virtual environment and installs the project dependencies for development.

**Raspberry Pi OS** - run these first

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-picamera2 python3-venv
```

Then:

```bash
make setup-pi
```

Installs the Raspberry Pi-specific dependencies and creates the virtual environment.

---

### 3. Run

```bash
make run
```

> **Development mode:** Press space or left-click inside the window to trigger the shutter. Captured photos are saved to `./captures/` instead of being printed.

---

## Installing Python with pyenv

_(Optional) Install pyenv to manage Python versions:_

If your Python version is between 3.10 and 3.13 you can skip this section.

3.14 may work but some dependencies don't have pre-built packages for it yet and may require additional system libraries to compile from source.

**Linux**

```bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash
```

**macOS**

Install [Homebrew](https://brew.sh) if you don't have it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
brew install pyenv
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

---

## Troubleshooting

### Stretched or wrong camera feed

Run this to list all available cameras and their native resolutions:

```bash
make camera-list
```

Update the corresponding values in `config.py` to match your camera's native resolution.

### Terminal not finding pyenv

If you get `pyenv: command not found`, make sure you added the pyenv config to your `~/.zshrc` (or `~/.bashrc`) and ran `source ~/.zshrc`. On Linux, also check that your terminal is not installed via Snap, as Snap sandboxing can block pyenv's access to system files.
