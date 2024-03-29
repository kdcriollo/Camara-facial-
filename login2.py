# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import cv2

us="GENESIS"
psw="12345"



class Ui_MainWindow(object):
    
    def __init__(self):
        self.NOMBRE="0"
        self.CLAVE="0"
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:11.3, stop:0.738636 rgba(95, 95, 95, 255), stop:0.982955 rgba(200, 237, 255, 255));\n"
"border-radius:20px;\n"
"border:1px solid #000000;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(450, 50, 191, 121))
        self.label.setStyleSheet("border:none")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("faci.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 151, 51))
        self.label_2.setStyleSheet("background-color: rgba(0, 0,0, 0%);\n"
"font: 16pt \"Swis721 BlkEx BT\";\n"
"border:none")
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(2)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 101, 51))
        self.label_3.setStyleSheet("background-color: rgba(0, 0,0, 0%);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 11pt \"Arial Black\";\n"
"\n"
"border:none")
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(2)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 151, 51))
        self.label_4.setStyleSheet("background-color: rgba(0, 0,0, 0%);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 11pt \"Arial Black\";\n"
"\n"
"border:none")
        self.label_4.setWordWrap(False)
        self.label_4.setIndent(2)
        self.label_4.setObjectName("label_4")
        self.user = QtWidgets.QLineEdit(self.frame)
        self.user.setGeometry(QtCore.QRect(130, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user.setFont(font)
        self.user.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.user.setAlignment(QtCore.Qt.AlignCenter)
        self.user.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.user.setClearButtonEnabled(False)
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(150, 200, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.Ingresar = QtWidgets.QPushButton(self.frame)
        self.Ingresar.setGeometry(QtCore.QRect(360, 280, 101, 41))
        self.Ingresar.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(111, 198, 211);\n"
"    font: 87 11pt \"Arial Black\";\n"
"    border: 5px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(128, 255, 82);\n"
"    \n"
"    font: 87 11pt \"Arial Black\";\n"
"    border: 5px solid #ffffff;\n"
"}")
        self.Ingresar.setObjectName("Ingresar")
        self.Cancelar = QtWidgets.QPushButton(self.frame)
        self.Cancelar.setGeometry(QtCore.QRect(480, 280, 101, 41))
        self.Cancelar.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(111, 198, 211);\n"
"    font: 87 11pt \"Arial Black\";\n"
"    border: 5px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    \n"
"    background-color: rgb(222, 37, 40);\n"
"    \n"
"    font: 87 11pt \"Arial Black\";\n"
"    border: 5px solid #ffffff;\n"
"}")
        self.Cancelar.setObjectName("Cancelar")
        
        self.contrasena_incorrecta = QtWidgets.QLabel(self.frame)
        self.contrasena_incorrecta.setGeometry(QtCore.QRect(350, 220, 291, 41))
        self.contrasena_incorrecta.setStyleSheet("background-color: rgba(0, 0,0, 0%);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(156, 26, 0);\n"
"border:none")
        
        
        
        self.contrasena_correcta = QtWidgets.QLabel(self.frame)
        self.contrasena_correcta.setGeometry(QtCore.QRect(350, 220, 291, 41))
        self.contrasena_correcta.setStyleSheet("background-color: rgba(0, 0,0, 0%);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 120, 0);\n"
"border:none")
        
        self.excede_dimension = QtWidgets.QLabel(self.frame)
        self.excede_dimension.setGeometry(QtCore.QRect(60, 330, 500, 41))
        self.excede_dimension.setStyleSheet("background-color: rgba(0, 0,0, 0%);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border:none")        
        
                          
        
        
        
        self.contrasena_incorrecta.setWordWrap(False)
        self.contrasena_incorrecta.setIndent(2)
        self.contrasena_incorrecta.setObjectName("contrasena_incorrecta")
       
        self.contrasena_correcta.setWordWrap(False)
        self.contrasena_correcta.setIndent(2)
        self.contrasena_correcta.setObjectName("contrasena_correcta")
        
        self.excede_dimension.setWordWrap(False)
        self.excede_dimension.setIndent(2)
        self.excede_dimension.setObjectName("excede_dimension")
        
        
        
        
        
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        
        #self.contrasena_incorrecta.linkActivated['QString'].connect(self.Ingresar.click) # type: ignore
        #self.contrasena_correcta.linkActivated['QString'].connect(self.Ingresar.click) # type: ignore
        
        
        
        
        self.password.textEdited['QString'].connect(self.password.setText) # type: ignore
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.contrasena_incorrecta.hide()==True
        self.contrasena_correcta.hide()==True
        self.excede_dimension.hide()==True        
        
        self.Ingresar.clicked.connect(self.INGRESAR)
        self.Cancelar.clicked.connect(self.CANCELAR)
    
        
    
    
    
    
    
    def INGRESAR(self):
        usuario=self.user.text()
        contrasena=self.password.text()
        
        u=len(usuario)
        p=len(contrasena)
        
        self.user.clear()
        self.password.clear()
        
        
        uc=self.usuario_correct(u)
        pc=self.clave_correct(p)
      
        
        if uc==1 and pc==1:
                          
                       
            if usuario==us and contrasena==psw:
                self.contrasena_correcta.show()==True
                self.contrasena_incorrecta.hide()==True
                self.CANCELAR()
                from gene import frame
                
                
                
                
            else:
                self.contrasena_incorrecta.show()==True
                self.contrasena_correcta.hide()==True
            
        else:
                self.excede_dimension.show()==True
                self.excede_dimension.show()==True
                self.contrasena_incorrecta.hide()==True
                self.contrasena_correcta.hide()==True
        
        
        
    
    
    def usuario_correct(self, u):
        if u<=8 and u>4:
            return 1
        else:
            return "Usuario debe tener 5-8 digitos"
        
    def usuario_incorrect(self, u):
        if u!="GENESIS":
            return "Usuario incorrecto"
    
    def clave_correct(self,p):
        if p<=6 and p>3:
            return 1
        else:
            return "Contrasena debe tener 4-6 digitos"
        
    def clave_incorrect(self,p):
        if p!="12345":
            return "Contrasena incorrecta"
    
    
    
    def Setear_usuario(self,valor):
        self.NOMBRE=valor
        
    def Setear_clave(self,valor):
        self.CLAVE=valor
        
    def Obtener_usuario(self):
        return self.NOMBRE
        
    def Obtener_clave(self):
        return self.CLAVE
        
        
 #TEST FUNCIONAMIENTO       
    def ojos_cerrados(self,ear):
         if ear < 0.2:
             return "Ojos cerrados"
         
    def ojos_abiertos(self,ear):
         if ear > 0.2:
             return "Ojos abiertos"
         
    def ojos(self,ear):
         if ear < 0.2:
             return " "
         
    def tiempo(self,tiemp):
         if tiemp>=5:
             return"Alarma activada"
         else:
             return" "    
             
    def conteo_activacion(self,alarma):
        if alarma>=1:
            return(alarma)
        else:
            return ("La alarma no se activo")
        
    def tiempo_activacion(self,tiempo):
        if tiempo>=8:
            return("Time out")
        else:
            return ("")
    def boton_act(self,valor):
        if valor==1:
            return("EMERGENCIA")
        else:
            return (" ")     
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "INGRESO"))
        self.label_3.setText(_translate("MainWindow", "USUARIO:"))
        self.label_4.setText(_translate("MainWindow", "CONTRASEÑA:"))
        self.user.setPlaceholderText(_translate("MainWindow", "Ingrese el usuario"))
        self.password.setPlaceholderText(_translate("MainWindow", "Ingrese la contraseña"))
        self.Ingresar.setText(_translate("MainWindow", "Ingresar"))
        self.Cancelar.setText(_translate("MainWindow", "Cancelar"))
        
        
        
        self.contrasena_incorrecta.setText(_translate("MainWindow", "Usuario o contraseña incorrecta!!"))
        self.contrasena_correcta.setText(_translate("MainWindow", "INGRESO LISTO!"))
        self.excede_dimension.setText(_translate("MainWindow", "El usuario debe tener  5-8 digitos y la contraseña 4-6."))



    def CANCELAR(self):
        app.closeAllWindows()




import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())