# Run any command with: make <command>
# Example: make run

.PHONY: setup setup-pi run

setup:
	pyenv local 3.13
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

setup-pi:
	python3 -m venv .venv --system-site-packages
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python main.py