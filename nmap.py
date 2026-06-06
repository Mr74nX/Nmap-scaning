import os
import subprocess
os.system("git pull")
subprocess.run(["python3", "-c", "import nmap; nmap.menu()"])
