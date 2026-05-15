import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt
import pyautogui

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

class Overlay(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.show()
        
        self.rects = [(100, 100, 200, 100), (400, 300, 150, 150)]

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(255, 0, 0))  # red rectangles
        pen.setWidth(2)
        painter.setPen(pen)

        for x, y, w, h in self.rects:
            painter.drawRect(x, y, w, h)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    overlay = Overlay()

    sys.exit(app.exec())
    
    
# [python - Qt Widget with Transparent Background](https://www.iditect.com/program-example/python--qt-widget-with-transparent-background.html)