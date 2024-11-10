# archivo: LoadingAnimation.py

import sys
import threading
import time

class LoadingAnimation:
    def __init__(self, message="Procesando"):
        self.message = message
        self.running = False
        self.thread = None

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.animate)
        self.thread.start()

    def animate(self):
        while self.running:
            for frame in ['.', '..', '...']:
                sys.stdout.write(f'\r{self.message}{frame}')
                sys.stdout.flush()
                time.sleep(0.5)

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()
        sys.stdout.write('\r')  # Limpia la línea
        sys.stdout.flush()
