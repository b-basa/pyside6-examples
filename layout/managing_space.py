import sys
from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QWidget,
)

# .sizeHint() contains the widget’s recommended size
# .minimumSizeHint() contains the smallest size the widget can have while remaining usable
# .sizePolicy() holds the default behavior of a widget in a layout

# Managing Space in Box Layouts

# .addSpacing(i) adds a non-stretchable space (or empty box) of fixed size i to the layout. i must be an integer representing the size of the space in pixels.
# .addStretch(i) adds a stretchable space with a minimum size of 0 and a stretch factor i to a box layout. i must be an integer.
# .insertSpacing(index, size) inserts a non-stretchable space at position index, with size size. If index is negative, then the space is added at the end of the box layout.
# insertStretch(index, stretch) inserts a stretchable space at position index, with a minimum size of 0 and a stretch factor of stretch. If index is negative, then the space is added at the end of the box layout.

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Bottom"))
        # If stretch isn't added, widgets fill the area
        layout.addStretch()
        # Set the layout on the application's window
        self.setLayout(layout)

class Window_grid(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout Example")
        self.resize(270, 110)
        # Create a QHBoxLayout instance
        layout = QFormLayout()
        
        # Add widgets to the layout with predefined spacing
        layout.setVerticalSpacing(30)
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Job:", QLineEdit())
        emailLabel = QLabel("Email:")
        layout.addRow(emailLabel, QLineEdit())
        
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window_grid = Window_grid()
    window_grid.show()
    sys.exit(app.exec_())