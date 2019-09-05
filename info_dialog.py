# -*- coding: utf-8 -*-

import os

from qgis.PyQt import QtGui, uic
from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtWidgets import QDialog
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'info.ui'))


class InfoDialog(QDialog, FORM_CLASS):

    closingPlugin = pyqtSignal()
    
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()
