import subprocess

command = [
    'python', 'yolov5/train.py',
    '--img', '640',
    '--batch', '10',
    '--epochs', '75',
    '--data', 'yolov5/data.yaml',
    '--weights', 'yolov5m.pt',
    '--name', 'intruder_detector',
    '--workers', '0'
]

subprocess.run(command)