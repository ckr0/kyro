import subprocess

replit_cmd = "killall -q python3 > /dev/null 2>&1; pip install -r requirements.txt && python3 main.py"
subprocess.run(replit_cmd, shell=True)