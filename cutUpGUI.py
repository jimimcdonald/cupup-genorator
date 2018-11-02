'''
The all new all singing all dancing fancy pants cUT uP eNGINE.

By Jimi (and/or Issi)
'''

import random

from cutup import CutUp

from PyQt5.QtWidgets import (QFrame, QTextEdit, QHBoxLayout, QVBoxLayout,
                             QApplication, QGridLayout, QPushButton, QMessageBox)
from PyQt5.QtGui import (QIcon, QPixmap)


class CutUpApp(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("cUT Up eNGINE")
        self.setWindowIcon(QIcon("Cut.png"))
        self.CreateApp()


    def CreateApp(self):
        self.input_layout = QHBoxLayout()
        self.output_layout = QVBoxLayout()

        # Make the stuff!
        self.InputBox1 = QTextEdit("Paste some text here.")
        self.InputBox2 = QTextEdit("Paste some other text here.")
        self.GoButton = QPushButton("Cut Up")
        self.OutputBox = QTextEdit("Cut up comes out here.")

        # Make the layout
        self.input_layout.addWidget(self.InputBox1)
        self.input_layout.addWidget(self.InputBox2)

        self.output_layout.addWidget(self.GoButton)
        self.output_layout.addWidget(self.OutputBox)

        self.mainLayout = QGridLayout()

        self.mainLayout.addLayout(self.input_layout, 0, 1)
        self.mainLayout.addLayout(self.output_layout, 1, 1)

        self.setLayout(self.mainLayout)

        # Make the button work
        self.GoButton.clicked.connect(self.PrintStuff)

        # Expose yourself!
        self.show()


    def PrintStuff(self):
        input1 = self.InputBox1.toPlainText()
        input2 = self.InputBox2.toPlainText()

        self.OutputBox.setPlainText(CutUp(input1, input2))



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = CutUpApp()
    window.show()

    sys.exit(app.exec_())
