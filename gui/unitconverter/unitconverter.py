#!/usr/bin/env python2

import sys

from PyQt4 import QtGui, QtCore

from conversion import Data


class Converter(QtGui.QWidget):

    def __init__(self, app):
        super(Converter, self).__init__()
        self.app = app
        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont("SansSerif", 10))

        # Main Window
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("UnitConverter")
        self.setWindowIcon(QtGui.QIcon("data/calculator.png"))

        # Create the initial UI elements.
        self.create_data_ui()

        # Now, show it all.
        self.show()

    def clear_gui(self):
        "Delete elements so we can switch to a different conversion mode."
        for widget in self.app.allWidgets():
            if isinstance(widget, QtGui.QLineEdit):
                widget.deleteLater()
            if isinstance(widget, QtGui.QLabel):
                widget.deleteLater()

    def create_data_ui(self):

        self.data = Data()

        data = ["bits", "bytes", "KB", "KiB", "MB", "MiB",
                "GB", "GiB", "TB", "TiB", "PB", "PiB"]

        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3),
               (4, 0), (4, 1), (4, 2), (4, 3),
               (5, 0), (5, 1), (5, 2), (5, 3)]
        # GRID
        grid = QtGui.QGridLayout()
        # Dictionary that holds our QLineEdit fields for later use.
        self.edits = {unit: QtGui.QLineEdit() for unit in data}

        for i in range(len(pos)):
            # Since data is half as long as pos, we use floor division to get
            # the correct corresponding data index from i.
            datapos = data[i // 2]
            # Add a QLabel for uneven positions and QLineEdits for even ones.
            if i % 2:
                grid.addWidget(QtGui.QLabel(datapos), pos[i][0], pos[i][1])
            else:
                field = self.edits[datapos]
                # Align text on the right.
                field.setAlignment(QtCore.Qt.AlignRight)
                grid.addWidget(field, pos[i][0], pos[i][1])

        # BUTTONS
        dbtn = QtGui.QPushButton("Data", self)
        lbtn = QtGui.QPushButton("Length", self)
        vbtn = QtGui.QPushButton("Volume", self)
        nbtn = QtGui.QPushButton("Numbers", self)
#         dbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(dbtn)
        hbox.addWidget(lbtn)
        hbox.addWidget(vbtn)
        hbox.addWidget(nbtn)

        # Patch it all together in a vertical layout.
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(grid)
        self.setLayout(vbox)

    def precision_changed(self, text):
        self.data.precision = int(text)

    def update_data(self):
        for i in self.edits:
            i.setText(str(self.data.i))

    def megabytes_changed(self, text):

        try:
            self.data.megabytes = float(text)
        except ValueError:
            self.data.megabytes = 0


def main():
    app = QtGui.QApplication(sys.argv)

    c = Converter(app)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
