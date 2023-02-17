from PyQt5.QtWidgets import*
from PyQt5.uic import*
#************************************************
def fact_premier(x,n): 
    n = 0
    nb = 0
    i = 2
    while(x != 1):
        if(x % i == 0):
            nb = nb + 1
            x = x// i
        elif (nb != 0):
            t[n][fp] = i
            t[n][puis] = nb
            n = n + 1
            nb = 0
        i = i + 1
#*********************************************
def play():
    cha=fen.a.text()
    chb=fen.b.text()
    if (cha=="" or chb=="") and (cha < 2 or chb < 2):
        mess=QMessageBox.critical(fen,"alert","vous devais deja saisir a et b")
        
    
#************************************************
f = dict({"fp":int;"puis":int})
app=QApplication([])
fen=loadUi('Arithmetique.ui')
fen.b_ok.clicked.connect(play)
fen.show()
app.exec_()