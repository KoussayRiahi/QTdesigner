from PyQt5.QtWidgets import*
from PyQt5.uic import*
#*********
def play():
    cha=fen.a.text()
    chb=fen.b.text()
    a=int(cha)
    b=int(chb)
    s=a+b
    fen.res.setText(str(s))
#*****
def play1():
    fen.a.setText("")
    fen.b.setText("")
    fen.res.setText("")
#******pp*****
app=QApplication([])
fen=loadUi('somme2entier.ui')
fen.b_somme.clicked.connect(play)
fen.b_effacer.clicked.connect(play1)
fen.show()
app.exec_()