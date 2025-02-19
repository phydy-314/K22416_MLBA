from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Salemanagement.libs.nhanvienconnector import NhanVienConnector
from Salemanagement.ui.LoginMainWindow import Ui_MainWindow
from Salemanagement.ui.MainprogramMainWindowExt import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.nvconnector = NhanVienConnector()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.SetupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def SetupSignalAndSlot(self):
        self.signinButton.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        try:
            username = self.Line_Edit_username.text().strip()
            password = self.Line_Edit_password.text().strip()

            self.nvconnector.connect()
            self.nvlogin = self.nvconnector.dang_nhap(username, password)

            if self.nvlogin != None:
            # if username == 'admin' and password == '123':
                print("Đăng nhập thành công")
                self.MainWindow.hide()
                self.mainwindow = QMainWindow()
                self.myui = MainProgramMainWindowExt()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
            else:
                print("Đăng nhập thất bại ")
                self.msg = QMessageBox()
                self.msg.setWindowTitle('Login Thất Bại')
                self.msg.setText('Sai username hoặc password. Vui lòng thử lại.')
                self.msg.setIcon(QMessageBox.Icon.Critical)
                self.msg.exec()
        except Exception as e:
            print(f" Lỗi xảy ra: {e}")

