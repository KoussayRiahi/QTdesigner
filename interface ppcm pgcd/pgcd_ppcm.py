from PyQt5.QtWidgets import*
from PyQt5.uic import*
#******
def pgcd(a,b):
    while (a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a
#*******
def ppcm(a,b):
    if(a>b):
        sup=a
        inf=b
    else:
        sup=b
        inf=a
    i=1
    while ((sup*i)%inf!=0):
        i=i+1
    return sup*i
#*********
def play():
    cha=fen.a.text()
    chb=fen.b.text()
    if cha=="" or chb=="":
        mess=QMessageBox.critical(fen,"alert","vous devais deja saisir a et b")
    else:
        a=int(cha)
        b=int(chb)   
        if fen.r1.isChecked():
            r=pgcd(a,b)
        if fen.r2.isChecked():
            r=ppcm(a,b)
        fen.res.setText(str(r))  
    
#******pp*****
app=QApplication([])
fen=loadUi('pgcd_ppcm.ui')
fen.b_affiche.clicked.connect(play)
fen.show()
app.exec_()