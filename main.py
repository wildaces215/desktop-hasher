from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox

from PyQt5 import *
import hashlib
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'File Hasher'
        self.left = 10
        self.top = 10
        self.width = 100
        self.height = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        grid = QGridLayout()
        hashLabel=QLabel("")
        
        uploadButton = QPushButton("Upload File",self)
        uploadButton.setToolTip('This is an example button')
        uploadButton.clicked.connect(self.uploadFile)
        grid.addWidget(uploadButton, 1, 0)
        grid.addWidget(hashLabel,2,0)
        self.setLayout(grid)
        
       
        
        
        
        self.show()
   
    @pyqtSlot()
    def uploadFile(self):
        filepath,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', options=QtWidgets.QFileDialog.DontUseNativeDialog)
        self.hash(filepath)
    
    def hash(self, file):
        hasher = hashlib.sha256()
        with open(file,'rb') as file:
            buf = file.read()
            hasher.update(buf)
        QMessageBox.about(self,"Hash",hasher.hexdigest())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())