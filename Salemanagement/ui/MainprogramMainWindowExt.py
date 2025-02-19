import sys

from PyQt6.QtWidgets import QMainWindow

from Salemanagement.ui.MainProgramMainWindow import Ui_MainWindow
from Salemanagement.ui.ProductMainWindowExt import ProductMainWindowExt


class MainProgramMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):  # Fix: Change "SetupUi" to "setupUi"
        super().setupUi(MainWindow)  # Calls parent setupUi method
        self.MainWindow = MainWindow  # Ensure MainWindow is stored
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.actionthoatphanmem.triggered.connect(self.xuly_thoat)
        self.actionQuanLySanPhamDanhMuc.triggered.connect(self.xuly_momanhinh_qlspdm)

    def xuly_thoat(self):
        sys.exit(0)

    def xuly_momanhinh_qlspdm(self):
        self.mainwindow = QMainWindow()
        self.myui = ProductMainWindowExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()