from PySide6.QtWidgets import QApplication, QMainWindow,QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.windowTitleChanged.connect(self.onWindowTitleChange)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))


        self.setWindowTitle("My Awesome App")

        label = QLabel("This is AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)


    
    def onWindowTitleChange(self, s):
        print(s)

    def my_custom_fn(self, a ="HEllo!!!", b=5):
        print(a, b)



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()