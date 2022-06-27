from PyQt5.QtWidgets import (
    QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
    QPushButton, QGridLayout
)

from PyQt5 import QtCore

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.setWindowTitle('FINAL Project')
        self.resize(350, 300)
        
        self.add_btn = QPushButton('Add Subject')
        self.calculate_btn = QPushButton('Calculate GPA')
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Subject', 'Score'])
        self.score = 0
        self.A = 0
        self.Am = 0
        self.Bp = 0
        self.B = 0
        self.Bm = 0
        self.Cp = 0
        self.C = 0
        self.D = 0
        self.E = 0 
        self.gpa = 0
        self.tot_cred = 0

        self.layout.addRow(self.add_btn)
        self.layout.addRow(self.calculate_btn)
        self.layout.addRow(self.table)

        self.add_btn.clicked.connect(self.add_subject)
        self.table.itemChanged.connect(self.on_change)
        self.calculate_btn.clicked.connect(self.calculate)
        
    def add_subject(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

    def on_change(self, item):
        col = item.column()
        row = item.row()
        grade = ''
        credit = 3       

        if col == 1 and not item.text().isnumeric():
            item.setText('')
        if col == 1 and item.text().isnumeric():
            temp = float(item.text())
            if col == 1 and (temp < 0 or temp > 100):
                item.setText('')
            if temp >= 85 and temp <= 100:
                grade = 'A'
                index = 4.00
                self.A = self.A + 1
                score_A = credit * index
                self.score = self.score + score_A
                # print(grade)
            elif temp < 85 and temp >= 80:
                grade = 'A-'
                index = 3.67
                self.Am = self.Am + 1
                score_Am = credit * index
                self.score = self.score + score_Am
                # print(grade)
            elif temp < 80 and temp >= 75:
                grade = 'B+'
                index = 3.33
                self.Bp = self.Bp + 1
                score_Bp = credit * index
                self.score = self.score + score_Bp
                # print(grade)
            elif temp < 75 and temp >=70:
                grade = 'B'
                index = 3.00
                self.B = self.B + 1
                score_B = credit * index
                self.score = self.score + score_B
                # print(grade)
            elif temp < 70 and temp >= 67:
                grade = 'B-'
                index = 2.67
                self.Bm = self.Bm + 1
                score_Bm = credit * index
                self.score = self.score + score_Bm
                # print(grade)
            elif temp < 67 and temp >= 64:
                grade = 'C+'
                index = 2.33
                self.Cp = self.Cp + 1
                score_Cp = credit * index
                self.score = self.score + score_Cp
                # print(grade)
            elif temp < 64 and temp >= 60:
                grade = 'C'
                index = 2.00
                self.C = self.C + 1
                score_C = credit * index
                self.score = self.score + score_C
                # print(grade)
            elif temp < 60 and temp >= 55:
                grade = 'D'
                index = 1
                self.D = self.D + 1
                score_D = credit * index
                self.score = self.score + score_D
                # print(grade)
            else:
                grade = 'E'
                index = 0
                self.E = self.E + 1
                score_E = credit * index
                self.score = self.score + score_E
                # print(grade)

            # print(self.score)
        
        empty = ''
        if self.table.cellEntered == empty:
            credit = 0
        self.tot_cred = credit * self.table.rowCount()
        self.gpa = self.score / self.tot_cred
        # print('GPA ' + str("{:.2f}".format(self.gpa)))
        
    def calculate(self):
        self.second_window = Second_Window(self)
        self.second_window.show()
        self.second_window.A_In.setText(str(self.A))
        self.second_window.Am_In.setText(str(self.Am))
        self.second_window.Bp_In.setText(str(self.Bp))
        self.second_window.B_In.setText(str(self.B))
        self.second_window.Bm_In.setText(str(self.Bm))
        self.second_window.Cp_In.setText(str(self.Cp))
        self.second_window.C_In.setText(str(self.C))
        self.second_window.D_In.setText(str(self.D))
        self.second_window.E_In.setText(str(self.E))
        self.second_window.gpa.setText(str("{:.2f}".format(self.gpa)))
        self.second_window.idx_in.setText( str("{:.2f}".format(self.score)))
        self.second_window.cred_in.setText(str(self.tot_cred))

class Second_Window(QWidget):
    def __init__(self, main_window):
        QWidget.__init__(self)
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.resize(500, 400)
        self.setWindowTitle('GPA Report')

        self.main_window = main_window
        self.label = QLabel('GPA:')
        self.label.setStyleSheet('''font: bold 45px; color: red;''')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.gpa = QLabel('')
        self.gpa.setStyleSheet('''font: bold 40px; color: green;''')
        self.gpa.setAlignment(QtCore.Qt.AlignCenter)
        self.result = QLabel('Result: ')
        self.A = QLabel('A: ')
        self.Am = QLabel('A-: ')
        self.Bp = QLabel('B+: ')
        self.B = QLabel('B: ')
        self.Bm = QLabel('B-: ')
        self.Cp =QLabel('C+: ')
        self.C = QLabel('C: ')
        self.D =QLabel('D: ')
        self.E = QLabel('E: ')
        self.tot_idx = QLabel('Total Index: ')
        self.tot_cred = QLabel('Total Credits: ')
        self.okk = QPushButton('Ok')
        
        self.okk.clicked.connect(self.ok_btn)

        self.A_In = QLabel('')
        self.Am_In = QLabel('')
        self.Bp_In = QLabel('')
        self.B_In = QLabel('')
        self.Bm_In = QLabel('')
        self.Cp_In =QLabel('')
        self.C_In = QLabel('')
        self.D_In =QLabel('')
        self.E_In = QLabel('')
        self.idx_in = QLabel('')
        self.cred_in = QLabel('')
        
        self.layout.addRow(self.label)
        self.layout.addRow(self.gpa)
        self.layout.addRow(self.result)
        self.layout.addRow(self.A, self.A_In)
        self.layout.addRow(self.Am, self.Am_In)
        self.layout.addRow(self.Bp, self.Bp_In)
        self.layout.addRow(self.B, self.B_In)
        self.layout.addRow(self.Bm, self.Bm_In)
        self.layout.addRow(self.Cp, self.Cp_In)
        self.layout.addRow(self.C, self.C_In)
        self.layout.addRow(self.D, self.D_In)
        self.layout.addRow(self.E, self.E_In)
        self.layout.addRow(self.tot_idx, self.idx_in)
        self.layout.addRow(self.tot_cred, self.cred_in)
        self.layout.addRow(self.okk)

    def ok_btn(self):
        self.close()
        

app = QApplication([])
window = Window()
window.show()
app.exec_()