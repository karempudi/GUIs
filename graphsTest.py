from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pyqtgraph as pg
from random import randint

class GraphWindow(QMainWindow):

    def __init__(self):
        super(GraphWindow, self).__init__()
        self.setWindowTitle("Graphics window")

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))
        self.y = [randint(0, 100) for _ in range(100)]

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)


        # timing the animation
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]
        self.y.append(randint(0, 100))

        self.data_line.setData(self.x, self.y)

if __name__ == "__main__":
    print("Graph animation plotter tests")
    app = QApplication()
    window = GraphWindow()
    window.show()
    app.exec()


