from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setWindowTitle("POS Application")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        self.label = QtWidgets.QLabel("Product", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 50, 20))
        self.label_2 = QtWidgets.QLabel("Quantity", self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 50, 20))
        self.label_3 = QtWidgets.QLabel("Discount", self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 50, 20))
        self.label_4 = QtWidgets.QLabel("Total", self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 50, 20))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 30, 180, 22))
        self.comboBox.addItems([
            "Body Vest Black Mamba (Rp. 512000)",
            "Sarung Hp Pinggang (Rp. 40000)",
            "Sarung Botol Tactical (Rp. 35000)",
            "Riot Control Helmet (Rp. 1150000)"
        ])

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 60, 20))
        self.lineEdit.setValidator(QtGui.QIntValidator(1, 999))

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 90, 60, 22))
        self.comboBox_2.addItems(["0%", "5%", "10%", "15%"])

        self.pushButton = QtWidgets.QPushButton("Add to Cart", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 100, 25))
        self.pushButton.clicked.connect(self.add_to_cart)
        
        self.pushButton_2 = QtWidgets.QPushButton("Clear", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 130, 100, 25))
        self.pushButton_2.clicked.connect(self.clear_cart)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 160, 220, 60))
        self.textEdit.setReadOnly(True)
        
        self.totalLabel = QtWidgets.QLabel("Rp. 0", self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(100, 230, 100, 20))

        self.label_name = QtWidgets.QLabel("Apta Mahogra Bhamakerti", self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(40, 260, 220, 20))
        
        self.label_nim = QtWidgets.QLabel("NIM : F1D022035", self.centralwidget)
        self.label_nim.setGeometry(QtCore.QRect(40, 280, 220, 20))
        
        self.label_nim = QtWidgets.QLabel("Kelas : C", self.centralwidget)
        self.label_nim.setGeometry(QtCore.QRect(40, 300, 220, 20))

        MainWindow.setCentralWidget(self.centralwidget)

        self.total = 0  


    def add_to_cart(self):
        product_data = {
            "Body Vest Black Mamba": 512000,
            "Sarung Hp Pinggang": 40000,
            "Sarung Botol Tactical": 35000,
            "Riot Control Helmet": 1150000
        }

        selected_product = self.comboBox.currentText()
        product_name, price = selected_product.rsplit(" (Rp. ", 1)
        price = int(price.rstrip(")"))

        try:
            quantity = int(self.lineEdit.text())
        except ValueError:
            quantity = 1

        discount = int(self.comboBox_2.currentText().rstrip("%"))
        
        subtotal = price * quantity
        discount_amount = (subtotal * discount) // 100
        final_price = subtotal - discount_amount

        self.total += final_price

        self.textEdit.append(f"{product_name} x{quantity} - Discount {discount}% => Rp. {final_price}")
        self.totalLabel.setText(f"Rp. {self.total}")

    def clear_cart(self):
        self.textEdit.clear()
        self.total = 0
        self.totalLabel.setText("Rp. 0")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
