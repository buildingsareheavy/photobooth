# Run any command with: make <command>
# Example: make run

.PHONY: setup setup-pi run camera-list

setup:
	pyenv local 3.13
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

setup-pi:
	python3 -m venv .venv --system-site-packages
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python main.py

camera-list:
	.venv/bin/python -c "\
import cv2, os, sys; \
os.environ['OPENCV_LOG_LEVEL'] = 'SILENT'; \
found = False; \
[print(f'Index {i}: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}') or cap.release() \
for i in range(5) if (cap := cv2.VideoCapture(i)).isOpened() and (found := True)] or \
print('No cameras found.') if not found else None \
" 2>/dev/null