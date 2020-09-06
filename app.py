from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(400,200, 1000,800)
	win.setWindowTitle('이너프 샐러드')

	label = QtWidgets.QLabel(win)
	label.setText('Label')
	label.move(50,50)

	win.show()
	sys.exit(app.exec_())
window()