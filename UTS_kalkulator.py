from UTS_kalkulatorGui import*
""" """
def signals(self):
    self.pushButton.clicked.connect(self.calc)
    self.pushButton.clicked.connect(self.click_jumlah)
    self.pushButton_div.clicked.connect(self.click_div)
    self.pushButton_x.clicked.connect(self.click_x)
    self.pushButton_plus.clicked.connect(self.click_plus)
    self.pushButton_minus.clicked.connect(self.click_minus)
    self.pushButton_clear.clicked.connect(self.click_clear)
    self.pushButton_del.clicked.connect(self.click_del)
    self.pushButton_1.clicked.connect(self.click1)
    self.pushButton_2.clicked.connect(self.click2)
    self.pushButton_3.clicked.connect(self.click3)
    self.pushButton_4.clicked.connect(self.click4)
    self.pushButton_5.clicked.connect(self.click5)
    self.pushButton_6.clicked.connect(self.click6)
    self.pushButton_7.clicked.connect(self.click7)
    self.pushButton_8.clicked.connect(self.click8)
    self.pushButton_9.clicked.connect(self.click9)
    self.pushButton0.clicked.connect(self.click0)
    self.pushButton0_3.clicked.connect(self.click0_3)
    self.pushButton_point.clicked.connect(self.click_point)

    
#operator box    
def calc(self) :
    a = int(self.lineEdit_1.text())
    b = int(self.lineEdit_2.text())
    operator = self.comboBox.currentText()
    try: 
        if operator == "+":
            result = a + b
            self.label.setText(str(result))
        elif operator == "-" :
            result = a - b
            self.label.setText(str(result))
        elif operator == "x" :
            result = a * b
            self.label.setText(str(result))
        elif operator == "/" :
            result = a / b
            self.label.setText(str(result))
        elif operator == "%" :
            result = a / 100 * b
            self.label.setText(str(result))
        else :
            result = "Not found"
            self.label.setText(str(result))
    except :
            self.label.setText('Error!!!')
#operator button
def click_jumlah(self) :
    jumlah = self.label.text()
    try :
        result =eval(jumlah)
        self.label.setText(str(result))
    except :
        self.label.setText('Error!!!')
def click_div(self):
    text = self.label.text()
    self.label.setText(text + "/")
def click_x(self):
    text = self.label.text()
    self.label.setText(text + "*")
def click_plus(self):
    text = self.label.text()
    self.label.setText(text + "+")
def click_minus(self):
    text = self.label.text()
    self.label.setText(text + "-")
#delete
def click_clear(self):
    self.label.setText("")
    self.lineEdit_1.clear()
    self.lineEdit_2.clear()
def click_del(self):
    text = self.label.text()
    print(text[:len(text)-1])
    self.label.setText(text[:len(text)-1])

#number button
def click1(self):
    text = self.label.text()
    self.label.setText(text + "1")
def click2(self):
    text = self.label.text()
    self.label.setText(text + "2")
def click3(self):
    text = self.label.text()
    self.label.setText(text + "3")
def click4(self):
    text = self.label.text()
    self.label.setText(text + "4")
def click5(self):
    text = self.label.text()
    self.label.setText(text + "5")
def click6(self):
    text = self.label.text()
    self.label.setText(text + "6")
def click7(self):
    text = self.label.text()
    self.label.setText(text + "7")
def click8(self):
    text = self.label.text()
    self.label.setText(text + "8")
def click9(self):
    text = self.label.text()
    self.label.setText(text + "9")
def click0(self):
    text = self.label.text()
    self.label.setText(text + "0")
def click0_3(self):
    text = self.label.text()
    self.label.setText(text + "000")
def click_point(self):
    text = self.label.text()
    self.label.setText(text + ".")

Ui_MainWindow.signals = signals
Ui_MainWindow.calc =calc
Ui_MainWindow.click_jumlah = click_jumlah
Ui_MainWindow.click_div = click_div
Ui_MainWindow.click_x = click_x
Ui_MainWindow.click_plus = click_plus
Ui_MainWindow.click_minus = click_minus
Ui_MainWindow.click_clear = click_clear
Ui_MainWindow.click_del = click_del
Ui_MainWindow.click1 = click1
Ui_MainWindow.click2 = click2
Ui_MainWindow.click3 = click3
Ui_MainWindow.click4 = click4
Ui_MainWindow.click5 = click5
Ui_MainWindow.click6 = click6
Ui_MainWindow.click7 = click7
Ui_MainWindow.click8 = click8
Ui_MainWindow.click9 = click9
Ui_MainWindow.click0 = click0
Ui_MainWindow.click0_3 = click0_3
Ui_MainWindow.click_point = click_point



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())