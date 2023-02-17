from PyQt5.QtWidgets import*
from PyQt5.uic import*

#************************************************

def play():
    chn=fen.n.text()
    if chn =="":
        msg = QMessageBox.critical(fen,"alerte","le nbr est vide !!!")
        
    else:
        if not(chn.isdigit() and 5<=int(chn)<=30):
            msg = QMessageBox.critical(fen,"alerte","le nbr doit etre un entier")
        
        else:
            msg = QMessageBox.information(fen,"alerte","le nbr doit etre entre 5 et 50 !!")

#************************************************
def play1():
    return
#************************************************
def play2():
    return
def play3():
    return


#*************************************************
app=QApplication([])
fen=loadUi("gestion eleves.ui")
fen.b_verifier.clicked.connect(play)
fen.b_ajouter.clicked.connect(play1)
fen.b_effacer.clicked.connect(play2)
fen.b_afficher.clicked.connect(play3)
fen.show()
app.exec_()