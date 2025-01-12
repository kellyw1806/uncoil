import signal
import subprocess
import sys
import os

def run_servers():
    server_cmd = "powershell -ExecutionPolicy ByPass -Command \". .venv\\Scripts\\Activate.ps1; fastapi dev main.py\""
    client_cmd = "npm run dev"

    server_process = subprocess.Popen(server_cmd, cwd="server", shell=True)
    client_process = subprocess.Popen(client_cmd, cwd="client", shell=True)

    try:
        server_process.wait()
        client_process.wait()
    except KeyboardInterrupt:
        server_process.terminate()
        client_process.terminate()
        server_process.wait()
        client_process.wait()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments (\"run\" or \"install\") provided")
    elif sys.argv[1] == "run":
        run_servers()
