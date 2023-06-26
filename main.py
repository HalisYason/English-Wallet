
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt

from main_pages import mainPages
import sys


#  app  bu sayfadan çalıştırılır

app = QApplication(sys.argv)

window = mainPages()
window.show()


sys.exit(app.exec_())


