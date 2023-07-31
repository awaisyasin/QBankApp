import sys
from PyQt5.QtCore import Qt  # noqa: F401
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QLCDNumber,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Bank():
    def __init__(self, tot_amt=0, lst_dep_amt=0, lst_with_amt=0):
        self.tot_amt = tot_amt
        self.lst_dep_amt = lst_dep_amt
        self.lst_with_amt = lst_with_amt


    def dep_amt(self):
        amt = int(input.text())
        input.clear()
        self.lst_dep_amt = amt
        self.tot_amt += amt

        file = open('clientOne.txt', 'a')
        file.write('-----Wellcome to the bank app-----\n')
        file.write('---available amount---\n')
        file.write(f'{self.tot_amt}\n')
        file.write('---last deposited amount---\n')
        file.write(f'{self.lst_dep_amt}\n')
        file.write('---last withdrawn amount---\n')
        file.write(f'{self.lst_with_amt}\n')
        file.write('-----Thank you for using our app-----\n')
        file.close()

        Bank.check(self)

    def with_amt(self):
        amt = int(input.text())
        input.clear()
        self.lst_with_amt = amt
        if self.tot_amt < amt:
            input.setDisabled(True)
            input.setText('Your balance is not enough')
            input.setStyleSheet("color: red;")
        else:
            self.tot_amt -= amt

            file = open('clientOne.txt', 'a')
            file.write('-----Wellcome to the bank app-----\n')
            file.write('---available amount---\n')
            file.write(f'{self.tot_amt}\n')
            file.write('---last deposited amount---\n')
            file.write(f'{self.lst_dep_amt}\n')
            file.write('---last withdrawn amount---\n')
            file.write(f'{self.lst_with_amt}\n')
            file.write('-----Thank you for using our app-----\n')
            file.close()

            Bank.check(self)

    def check(self):
        with open('clientOne.txt', 'r') as file:
            lines = file.readlines()
            lcd.display(int(lines[-6]))
    def check2(self):
        with open('clientOne.txt', 'r') as file:
            lines = file.readlines()
            lcd.display(int(lines[-4]))
    def check3(self):
        with open('clientOne.txt', 'r') as file:
            lines = file.readlines()
            lcd.display(int(lines[-2]))

clientOne = Bank()
try:
    with open('clientOne.txt', 'r') as file:
        lines = file.readlines()
        tot_lines = len(lines)
    with open('clientOne.txt', 'r') as file:
        for i in range(tot_lines):
            line = file.readline()
            if i == tot_lines - 6:
                clientOne.tot_amt = int(line)
            if i == tot_lines - 4:
                clientOne.lst_dep_amt = int(line)
            if i == tot_lines - 2:
                clientOne.lst_with_amt = int(line)

except:
    file = open('clientOne.txt', 'w')
    file.write('-----Wellcome to the bank app-----\n')
    file.write('---available amount---\n')
    file.write('0\n')
    file.write('---last deposited amount---\n')
    file.write('0\n')
    file.write('---last withdrawn amount---\n')
    file.write('0\n')
    file.write('-----Thank you for using our app-----\n')
    file.close()


def performOperation():
    value = combo.currentText()
    if value == "Deposit":
        Bank.dep_amt(clientOne)
    elif value == "Withdraw":
        Bank.with_amt(clientOne)

def clearAll():
    input.setDisabled(False)
    input.setStyleSheet("color: black;")
    input.clear()
    input.setFocus()
    lcd.display(0)
    value = combo.currentText()
    if value == "Last Deposit Amount":
        Bank.check2(clientOne)
        input.setDisabled(True)
    elif value == "Last Withdraw Amount":
        Bank.check3(clientOne)
        input.setDisabled(True)
    elif value == "Current Amount":
        Bank.check(clientOne)
        input.setDisabled(True)
    elif value == "Exit":
        app.quit()


app = QApplication(sys.argv)
window = QWidget()

label1 = QLabel('Select an option')
combo = QComboBox()
combo.addItems(["--Select an option--", "Deposit", "Last Deposit Amount", "Withdraw", "Last Withdraw Amount", "Current Amount", "Exit"])
combo.activated.connect(clearAll)
label2 = QLabel('Enter amount')
input = QLineEdit()
input.setValidator(QIntValidator())
button = QPushButton('Submit')
button.clicked.connect(performOperation)
lcd = QLCDNumber()

box = QVBoxLayout()
box.addWidget(label1)
box.addWidget(combo)
box.addWidget(label2)
box.addWidget(input)
box.addWidget(button)
box.addWidget(lcd)

style = """
QPushButton {
    background-color: #4CAF50;
    color: white;
    padding: 8px 16px;
    text-align: center;
    font-size: 16px;
    border-radius: 8px;
}

QComboBox {
    background-color: #f2f2f2;
    border: 2px solid black;
    color: black;
    padding: 8px 16px;
    text-align: center;
    font-size: 16px;
    border-radius: 8px;
}

QLabel {
    font-size: 16px;
    font-weight: bold;
}

QLineEdit {
    background-color: #f2f2f2;
    border: 2px solid black;
    color: black;
    padding: 8px 16px;
    text-align: center;
    font-size: 16px;
    border-radius: 8px;
}

QLCDNumber {
    background-color: #f2f2f2;
    border: 2px solid black;
    padding: 8px 16px;
    text-align: center;
    font-size: 16px;
    border-radius: 8px;
}
"""

app.setStyleSheet(style)

window.setGeometry(600, 150, 200, 300)
window.setFixedSize(250, 350)
window.setWindowTitle("QBank")
window.setLayout(box)
window.show()
sys.exit(app.exec_())