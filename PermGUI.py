'''
The all new all singing all dancing fancy pants cUT uP eNGINE.

By Jimi (and/or Issi)
'''

import random

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

    def CutUp(self, input1, input2):

        wordlist1 = []
        wordlist2 = []
        output = []

        # Make word lists
        words = (input1.split())
        for word in words:
            wordlist1.append(word)

        words = (input2.split())
        for word in words:
            wordlist2.append(word)

        for self.i in range(10):
            if self.i % 2 == 0:
                wordlist = wordlist1
            else:
                wordlist = wordlist2


            start = random.randint(0, len(wordlist))
            end = start + random.randint(0, 10)
            output.append(' '.join(wordlist[start:end]))
            del(wordlist[start:end])
            print(output)


        return ' '.join(output)


    def PrintStuff(self):
        print("Cut Up!")
        input1 = self.InputBox1.toPlainText()
        input2 = self.InputBox2.toPlainText()

        self.OutputBox.setPlainText(self.CutUp(input1, input2))



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = CutUpApp()
    window.show()

    sys.exit(app.exec_())
