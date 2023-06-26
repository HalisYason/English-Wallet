

#     kullanıcı bilgilerini güncelleme  sayfası


from ui.kullanici_bilgi_ui import Ui_Form
from PyQt5.QtCore import QTimer,pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from database.database import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox



class kullanici(QWidget):
    kapanma_sinyal = pyqtSignal(bool)
    def __init__(self):
        super().__init__()
        self.main = Ui_Form()
        self.main.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        # filename değişkeni
        self.filename = ""

        # sinyal
        # self.kapanma_sinyal = pyqtSignal(bool)

################################################################    butonlar    #######################################################################
        self.main.pushButton_resim_sec.clicked.connect(self.resim_sec)
        self.main.pushButton_kullanici_bilgi_kaydet.clicked.connect(self.bilgileri_al)

####################################################      sayfa içi kodlar     ####################################################

    # kullanıcının resim seçmesini sağlar
    def resim_sec(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Resim Seç', '.', 'Resim (*.png *.jpg *.jpeg)')
        pixmap = QPixmap(self.filename)
        self.main.label_kullanici_foto.setPixmap(pixmap)
        self.main.label_kullanici_foto.setScaledContents(True)

    # kullanıcı biligileri ilk kez yenileniyor ise vt yazar değiştirme işlemi yapılıyorsa günceller
    def bilgileri_al(self):
        ad = self.main.lineEdit_kullanici_adi.text()
        resim = self.main.label_kullanici_foto.pixmap()

        if ad !="" and resim !=None:
            T, data = vt_kullanici_bilgisi_var_mı()

            if T:
                guncelle = vt_kullanici_bilgi_guncelle(self.filename, ad)
                if guncelle:
                    data = (self.filename, ad)
                    self.kapanma_sinyal.emit(guncelle)
                else:
                    pass
            else:
                ekle = vt_kullanici_bilgi_ekle(self.filename, ad)
                if ekle:
                    data = (self.filename, ad)
                    self.kapanma_sinyal.emit(ekle)
        else:
            # kullanıcı eğer bilgileri girmezse uyarı mesajı çakar
            QMessageBox.warning(self, "Uyarı", "bilgileri giriniz!", QMessageBox.Ok)


