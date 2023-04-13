from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

def test():
    text.setText(str(randint(1, 200000)))

app = QApplication([])
win = QWidget()

line = QVBoxLayout()

text = QLabel()
line.addWidget(text, alignment= Qt.AlignCenter)

random_btn = QPushButton('выбрать случайное число')
random_btn.clicked.connect(test)
line.addWidget(random_btn)

win.setLayout(line) #устанавливаем линию в окно
win.show()
app.exec()