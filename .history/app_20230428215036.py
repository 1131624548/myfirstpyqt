import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow

# app = QApplication(sys.argv)

# window = QMainWindow()
# window.show()

# # Start the event loop.
# app.exec()


# import sys
# from PyQt6.QtWidgets import QApplication, QPushButton

# app = QApplication(sys.argv)

# window = QPushButton("Push Me")
# window.show()

# app.exec()


# from PyQt6.QtWidgets import QApplication, QWidget

# # Only needed for access to command line arguments
# import sys

# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([]) works too.
# app = QApplication(sys.argv)

# # Create a Qt widget, which will be our window.
# window = QWidget()
# window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# # Start the event loop.
# app.exec()


# # Your application won't reach here until you exit and the event
# # loop has stopped.


