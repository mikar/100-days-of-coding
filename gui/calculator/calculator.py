#!/usr/bin/env python2

import sys

from PyQt4 import QtGui, QtCore



class GUICalculator(QtGui.QWidget):

    def __init__(self):
        super(GUICalculator, self).__init__()
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon("calculator.png"))

        grid = self.create_button_grid()

        mainlayout = QtGui.QVBoxLayout()
        mainlayout.addLayout(grid)

        self.setLayout(mainlayout)

    def create_button_grid(self):
        "Creates the grid of conversion unit QLineEdits and QLabels for a tab."
        # Dictionary that holds our QLineEdit fields for later use.
#         edits = {i[0]: SelectAllLineEdit() for i in units}
        labels = ["Close", "mrc", "m+", "m-", "Clear", "(", ")", "!",
                  "sqrt", "pow", "%", "/",
                  "7", "8", "9", "*", "4", "5", "6", "-",
                  "1", "2", "3", "+", "0", ".", "C", "="]

        # Create our positions grid (0,0), (0,1) etc
        pos = [(i, j) for i in range(7) for j in range(4)]

        layout = QtGui.QGridLayout()

        for i in range(len(labels)):
            layout.addWidget(QtGui.QLabel(labels[i]), pos[i][0], pos[i][1])
            layout.addWidget(QtGui.QPushButton(labels[i]), pos[i][0], pos[i][1])

        return layout


def main():
    app = QtGui.QApplication(sys.argv)
    c = GUICalculator()
    c.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()