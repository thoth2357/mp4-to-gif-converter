import queue
import threading

class ThreadFunc(threading.Thread):
    def __init__(self, loop_time=1.0 / 60):
        super(ThreadFunc, self).__init__()
        self.queue = queue.Queue()
        self.timeout = loop_time
        self.parent = None
        self.stop_on_complete = None
        self.running = False
        self._stop = threading.Event()

    def start_thread(self, parent, stop_on_complete=False):
        # thread can wait for functions if not stop_on_complete
        self.parent = parent
        self.stop_on_complete = stop_on_complete
        self.running = True
        self.start()

    def put_function(self, function, *args, **kwargs):
        # put another function in queue
        self.queue.put((function, args, kwargs))

    def run(self):
        print('### STARTED ###')
        while self.running:
            try:
                function, args, kwargs = self.queue.get(timeout=self.timeout)
                print('### RUNNING ###')
                function(*args, **kwargs)
            except queue.Empty:
                if self.stop_on_complete:
                    self.stop()
                else:
                    self.idle()

    def stop(self):
        print('### STOPPED ###')
        self.running = False
        self._stop.set()

    @staticmethod
    def idle():
        print('### IDLE ###')

