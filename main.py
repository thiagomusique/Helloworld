from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLineEdit, QHBoxLayout, QMessageBox,
                             QRadioButton, QGroupBox, QVBoxLayout)
import sys


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # primeiros widgets
        self.button = QPushButton("Exibir mensagem")
        self.button.clicked.connect(self.exibir)
        self.line_edit = QLineEdit()

        # groupbox
        self.groupbox = QGroupBox("Opções de diálogo")

        # opcoes
        self.option_information = QRadioButton("Information")
        self.option_information.setChecked(True)
        self.option_warning = QRadioButton("Warning")
        self.option_critical = QRadioButton("Critical")

        # layout do groupbox
        self.layout_options = QVBoxLayout()
        self.layout_options.addWidget(self.option_information)
        self.layout_options.addWidget(self.option_critical)
        self.layout_options.addWidget(self.option_warning)
        self.groupbox.setLayout(self.layout_options)

        #layout do qpushbutton e qlineedit
        self.layout_first_widgets = QHBoxLayout()
        self.layout_first_widgets.addWidget(self.line_edit)
        self.layout_first_widgets.addWidget(self.button)

        # layout principal
        self.layout_master = QVBoxLayout()
        self.layout_master.addLayout(self.layout_first_widgets)
        self.layout_master.addWidget(self.groupbox)
        self.setLayout(self.layout_master)

    def exibir(self):
        text = self.line_edit.text()
        if self.option_information.isChecked():
            self.message_box = QMessageBox.information(self, "ex 01", text)

        elif self.option_warning.isChecked():
            self.message_box = QMessageBox.warning(self, "ex 02", text)

        else:
            self.message_box = QMessageBox.critical(self, "ex 03", text)


root = QApplication([])
app = Window()
app.show()
sys.exit(root.exec_())
