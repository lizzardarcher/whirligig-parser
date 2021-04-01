import sys

from transliterate import slugify
from PyQt5 import QtCore, QtGui, QtWidgets

from SearchForm import Ui_Form
from MainWindow import Ui_MainWindow
from Result import ResultWindow



data = {
    "searchRequest": "",
    "minPrice": "",
    "maxPrice": "",
    "searchRadius": "",
    "numPages": "",
    "registeredBeforeYear": "",
    "registeredAfterYear": "",
    "activeGoodMax": "",
    "activeGoodsMin": "",
    "viewsMax": "",
    "viewsMin": "",
    "adsPostedInThirtyDays": "",
    "reserved": "",
    "reserved_2": "",
    "reserved_3": "",
    "reserved_4": "",
    "city": "",
    "category": ""
}


def showResult():
    global Result
    Result = QtWidgets.QWidget()
    ui = ResultWindow()
    ui.setupUi(Result)
    Result.show()
    Form.close()


def showForm():
    def startSearchingEngine():
        searchRequest = ui.lineEdit.text()
        data["searchRequest"] = searchRequest

        minPrice = ui.lineEdit_2.text()
        data["minPrice"] = minPrice

        maxPrice = ui.lineEdit_3.text()
        data["maxPrice"] = maxPrice

        searchRadius = ui.lineEdit_4.text()
        data["searchRadius"] = searchRadius

        numPages = ui.lineEdit_5.text()
        data["numPages"] = numPages

        registeredBeforeYear = ui.lineEdit_6.text()
        data["registeredBeforeYear"] = registeredBeforeYear

        registeredAfterYear = ui.lineEdit_7.text()
        data["registeredAfterYear"] = registeredAfterYear

        activeGoodMax = ui.lineEdit_8.text()
        data["activeGoodMax"] = activeGoodMax

        activeGoodsMin = ui.lineEdit_9.text()
        data["activeGoodsMin"] = activeGoodsMin

        viewsMax = ui.lineEdit_10.text()
        data["viewsMax"] = viewsMax

        viewsMin = ui.lineEdit_11.text()
        data["viewsMin"] = viewsMin

        adsPostedInThirtyDays = ui.lineEdit_12.text()
        data["adsPostedInThirtyDays"] = adsPostedInThirtyDays

        reserved = ui.lineEdit_13.text()
        data["reserved"] = reserved

        reserved_2 = ui.lineEdit_14.text()
        data["reserved_2"] = reserved_2

        reserved_3 = ui.lineEdit_15.text()
        data["reserved_3"] = reserved_3

        reserved_4 = ui.lineEdit_16.text()
        data["reserved_4"] = reserved_4

        city = ui.comboBox.currentText()
        data["city"] = slugify(city).replace('j', 'y')

        category = ui.comboBox_2.currentText()
        data["category"] = slugify(category).replace("j", "y")

        print(data)

    global Form
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    MainWindow.close()
    ui.pushButton.clicked.connect(startSearchingEngine)
    ui.pushButton.clicked.connect(showResult)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uiMainWindow = Ui_MainWindow()
    uiMainWindow.setupUi(MainWindow)
    MainWindow.show()
    uiMainWindow.pushButton.clicked.connect(showForm)
    sys.exit(app.exec_())
