import sys
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QHBoxLayout Example")

        # Create a QHBoxLayout instance
        layout = QHBoxLayout()

        # Add widgets to the layout
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"), stretch=1)
        layout.addWidget(QPushButton("Right-Most"), stretch=2)

        # Set the layout on the application's window
        self.setLayout(layout)
        print(self.children())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
