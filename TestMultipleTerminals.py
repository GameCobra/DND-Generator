import subprocess

result = subprocess.run(["python", "Display.py"], shell=True, capture_output=True, text=True)

print(result.stdout)