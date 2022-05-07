from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout



app = QApplication([])
title = QLabel('Winner Winner Chicken Diner:')

my_win = QWidget()
my_win.setWindowTitle('randomizer')
my_win.move(900,70)

 

v_line = QVBoxLayout()
h_line = QHBoxLayout()

v_line.addWidget(
    title, alignment = Qt.AlignCenter
)
my_win.setLayout(v_line)
my_win.show()
app.exec_()