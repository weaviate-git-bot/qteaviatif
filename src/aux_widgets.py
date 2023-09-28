import sys
from PyQt5.QtWidgets import QApplication, QInputDialog, QComboBox, QCheckBox

def show_multi_select_dialog(items):
    # create an empty widget
    app = QApplication(sys.argv)
    # add a button to close the widget
    button = QCheckBox("Close")

    
    app.exec_()
    # Get the selected items



    