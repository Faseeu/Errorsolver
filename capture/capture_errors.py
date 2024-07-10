import subprocess
from threading import Thread

class ErrorCapture:
    def __init__(self):
        self.observers = []

    def attach_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def notify_observers(self, error_message):
        for observer in self.observers:
            observer.update(error_message)

    def capture_errors(self):
        process = subprocess.Popen(["python", "-u", "your_script.py"], stderr=subprocess.PIPE, universal_newlines=True)
        
        while True:
            error_line = process.stderr.readline()
            if error_line:
                self.notify_observers(error_line)
            else:
                break

    def start_capture(self):
        capture_thread = Thread(target=self.capture_errors)
        capture_thread.start()
