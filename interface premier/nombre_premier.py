from PyQt5.QtWidgets import*
from PyQt5.uic import*
#*****
def play():
    chb_res=fen.b_res.text()
    if chn=" "
        msg=QMessageBox.critical(fen,'alert',"donner nombre premier")
    else (b_res<0):
        msg=QMessageBox.critical(fen,'alert',"donner nombre premier suprieur a 0") 
        





#******
def premier():
a=True
for i in range (2,n):
    if(n%i):
        a=False
        return (a and n!=1)
#******pp*****
app=QApplication([])
fen=loadUi('interface_premieur.ui')
fen.b_affiche.clicked.connect(play)
fen.show()
app.exec_()
for i in range(1,1000):
    if premier(n):
        print(n)