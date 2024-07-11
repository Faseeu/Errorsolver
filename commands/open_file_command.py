import subprocess
from config.settings import VSCODE_PATH

def open_file(file, line):
    command = f"{VSCODE_PATH} -g {file}:{line}"
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Opened VS Code at {file}, line {line}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open VS Code: {e}")
