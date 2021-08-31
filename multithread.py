from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

import time
import traceback, sys

class WorkerSignals(QObject):


    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)

class Worker(QRunnable):
    '''
    Worker thread
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        '''
        Initialize teh runner function with passed args, kwargs
        '''

        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()
        self.l =QLabel("Start")
        b = QPushButton("Danger!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)


        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print("MultiThreading with maximum %d threads" % self.threadpool.maxThreadCount())


        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def execute_this_fn(self):
        for i in range(0, 5):
            time.sleep(1)
        return "Done"
    
    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!!!")

    def oh_no(self):
        worker = Worker(self.execute_this_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()
