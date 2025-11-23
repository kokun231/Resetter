#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout


class HelloPage(QDialog):
    """Simple dialog that displays a hello message."""

    def __init__(self, parent=None):
        super(HelloPage, self).__init__(parent)
        self.setWindowTitle("Hello")
        self.resize(320, 160)

        self.layout = QVBoxLayout(self)

        self.message_label = QLabel("Hello, Resetter!", self)
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)

        self.close_button = QPushButton("Close", self)
        self.close_button.setMaximumWidth(120)
        self.close_button.clicked.connect(self.close)

        self.layout.addWidget(self.message_label)
        self.layout.addWidget(self.close_button, 0, QtCore.Qt.AlignHCenter)
