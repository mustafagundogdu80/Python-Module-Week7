# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UserDialog(object):
    def setupUi(self, UserDialog):
        UserDialog.setObjectName("UserDialog")
        UserDialog.resize(346, 301)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        UserDialog.setFont(font)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::AddressBookNew")
        UserDialog.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(parent=UserDialog)
        self.frame.setGeometry(QtCore.QRect(0, 110, 351, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gbUserLogin = QtWidgets.QGroupBox(parent=self.frame)
        self.gbUserLogin.setGeometry(QtCore.QRect(10, 10, 331, 141))
        self.gbUserLogin.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        self.gbUserLogin.setObjectName("gbUserLogin")
        self.lUserName = QtWidgets.QLabel(parent=self.gbUserLogin)
        self.lUserName.setGeometry(QtCore.QRect(11, 30, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.lUserName.setFont(font)
        self.lUserName.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.lUserName.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lUserName.setObjectName("lUserName")
        self.leUserName = QtWidgets.QLineEdit(parent=self.gbUserLogin)
        self.leUserName.setGeometry(QtCore.QRect(122, 30, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setKerning(True)
        self.leUserName.setFont(font)
        self.leUserName.setToolTipDuration(1)
        self.leUserName.setInputMask("")
        self.leUserName.setText("")
        self.leUserName.setObjectName("leUserName")
        self.lePassword = QtWidgets.QLineEdit(parent=self.gbUserLogin)
        self.lePassword.setGeometry(QtCore.QRect(122, 60, 200, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setKerning(True)
        self.lePassword.setFont(font)
        self.lePassword.setToolTipDuration(1)
        self.lePassword.setText("")
        self.lePassword.setClearButtonEnabled(False)
        self.lePassword.setObjectName("lePassword")
        self.lPassword = QtWidgets.QLabel(parent=self.gbUserLogin)
        self.lPassword.setGeometry(QtCore.QRect(2, 60, 120, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.lPassword.setFont(font)
        self.lPassword.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.lPassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lPassword.setObjectName("lPassword")
        self.lLanguage = QtWidgets.QLabel(parent=self.gbUserLogin)
        self.lLanguage.setGeometry(QtCore.QRect(92, 110, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.lLanguage.setFont(font)
        self.lLanguage.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.lLanguage.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lLanguage.setObjectName("lLanguage")
        self.line = QtWidgets.QFrame(parent=self.gbUserLogin)
        self.line.setGeometry(QtCore.QRect(19, 90, 301, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.cbLanguage = QtWidgets.QComboBox(parent=self.gbUserLogin)
        self.cbLanguage.setGeometry(QtCore.QRect(210, 110, 111, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.cbLanguage.setFont(font)
        self.cbLanguage.setObjectName("cbLanguage")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.leUserName.raise_()
        self.lUserName.raise_()
        self.lePassword.raise_()
        self.lPassword.raise_()
        self.lLanguage.raise_()
        self.line.raise_()
        self.cbLanguage.raise_()
        self.ptLogin = QtWidgets.QPushButton(parent=self.frame)
        self.ptLogin.setGeometry(QtCore.QRect(70, 153, 131, 31))
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::GoHome")
        self.ptLogin.setIcon(icon)
        self.ptLogin.setObjectName("ptLogin")
        self.pbExit = QtWidgets.QPushButton(parent=self.frame)
        self.pbExit.setGeometry(QtCore.QRect(210, 153, 131, 31))
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::SystemLogOut")
        self.pbExit.setIcon(icon)
        self.pbExit.setObjectName("pbExit")
        self.frame_2 = QtWidgets.QFrame(parent=UserDialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 4, 351, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/WeRHere2.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        self.retranslateUi(UserDialog)
        QtCore.QMetaObject.connectSlotsByName(UserDialog)

    def retranslateUi(self, UserDialog):
        _translate = QtCore.QCoreApplication.translate
        UserDialog.setWindowTitle(_translate("UserDialog", "User Login Window"))
        self.gbUserLogin.setTitle(_translate("UserDialog", "User Login"))
        self.lUserName.setText(_translate("UserDialog", "User Name : "))
        self.lPassword.setText(_translate("UserDialog", "Password: "))
        self.lLanguage.setText(_translate("UserDialog", "Languages:"))
        self.cbLanguage.setItemText(0, _translate("UserDialog", "English"))
        self.cbLanguage.setItemText(1, _translate("UserDialog", "Nederlands"))
        self.cbLanguage.setItemText(2, _translate("UserDialog", "Türkçe"))
        self.ptLogin.setText(_translate("UserDialog", "Login"))
        self.ptLogin.setShortcut(_translate("UserDialog", "Return"))
        self.pbExit.setText(_translate("UserDialog", "Exit"))
        self.pbExit.setShortcut(_translate("UserDialog", "Ctrl+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserDialog = QtWidgets.QDialog()
    ui = Ui_UserDialog()
    ui.setupUi(UserDialog)
    UserDialog.show()
    sys.exit(app.exec())
