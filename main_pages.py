
#                                                     ENGLISH WALLET APP                                                   #


from PyQt5.QtWidgets import * 
from ui.uygulama_ui import Ui_MainWindow
from kullanici_page import kullanici
from database.database import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent


class mainPages(QMainWindow):

    def __init__(self):
        super().__init__() # üst sınıfın yapıcı yöntemini çağır
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        self.setWindowTitle("ENGLISH WALLET")
        # pencere boyutu ayarları
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setFixedSize(1314,800)

        self.statusBar().setStyleSheet("color: red")
       # oyna sayfası için gerekli
        self.kelime_sayac = 0
        self.cumle_sayac = 0

        self.kullanici_bilgi = kullanici()  # Qwidget sınıfı bir nesne oluşturduk

        # uygulama açılınca db den kullanıcı bilgilerini çeker
        self.yeni_kullanici_bilgileri()
        self.oyun_istatitik()
        self.oyun_ist_goster()

        #########################   oyun içi değişkenler
        # kelime
        self.main.pushButton_kelime_oyun_ileri.setText("İLERİ")
        self.main.pushButton_kelime_oyun_ileri.setEnabled(False)
        self.kelime_tur = ""
        self.kelime_soru_sayisi = 0
        self.kelime_dogru_sayisi = 0
        self.kelime_yanlis_sayisi = 0
        self.main.radioButton_kelime_oyun_kolay_mod.setChecked(True)
        self.kelime_oyun_mod_label()


        # cumle
        self.main.pushButton_cumle_oyun_ileri.setText("İLERİ")
        self.main.pushButton_cumle_oyun_ileri.setEnabled(False)
        self.cumle_oyun_soru_sayisi = 0
        self.cumle_oyun_dogru_sayisi = 0
        self.cumle_oyun_yanlis_sayisi = 0
        self.cumle_tur = ""
        self.main.radioButton_cumle_oyun_kolay_mod.setChecked(True)
        self.cumle_oyun_mod_label()

        ########################
    

####################################################################   butonlar   #######################################################################

###########   kullanici bilgileri düzenle  Qwidget
        self.main.pushButton_anasayfa_duzenle.clicked.connect(self.kullanici_bilgileri_duzenle)

########### stackedWidget currentIndexlerine ulaşan butonlar
        self.main.pushButton_yanmenu_anasayfa.clicked.connect(self.ana_page)
        self.main.pushButton_yanmenu_oyna.clicked.connect(self.oyna_page)
        self.main.pushButton_yanmenu_ekle.clicked.connect(self.ekle_page)
        self.main.pushButton_yanmenu_listele.clicked.connect(self.k_listele_page)
        self.main.pushButton_yanmenu_duzenle.clicked.connect(self.duzenle_page)
        self.main.pushButton_yanmenu_sil.clicked.connect(self.sil_page)
########### staticwidget 

    # oyna buton
        # kelime
        self.main.pushButton_kelime_oyun_ileri.clicked.connect(self.kelime_oyun_ileri_buton)
        self.main.pushButton_kelime_oyun_oyna.clicked.connect(self.kelime_oyun_oyna_buton)
        #cumle
        self.main.pushButton_cumle_oyun_ileri.clicked.connect(self.cumle_oyun_ileri_buton)
        self.main.pushButton_cumle_oyun_oyna.clicked.connect(self.cumle_oyun_oyna_buton)


    # ekle buton
        # kelime
        self.main.pushButton_kelime_ekle.clicked.connect(self.kelime_ekle)
        self.main.pushButton_kelime_ekle_geri.clicked.connect(self.k_listele_page)
        # cümle
        self.main.pushButton_cumle_ekle.clicked.connect(self.cumle_ekle)
        self.main.pushButton_cumle_ekle_geri.clicked.connect(self.c_listele_page)

    # düzenle buton
        # kelime
        self.main.pushButton_duzenle_kelime_guncelle.clicked.connect(self.kelime_duzenle)
        self.main.pushButton_duzenle_kelime_geri.clicked.connect(self.k_listele_page)
        #cümle
        self.main.pushButton_duzenle_cumle_guncelle.clicked.connect(self.cumle_duzenle)
        self.main.pushButton_duzenle_cumle_geri.clicked.connect(self.c_listele_page)

    # kelime ara buton
        # ara
        self.main.pushButton_listele_ara.clicked.connect(self.aranan_kelimeyi_listele)

    # sil buton
    # kelime
        self.main.pushButton_kelime_sil_geri.clicked.connect(self.k_listele_page)
        self.main.pushButton_kelime_sil.clicked.connect(self.kelime_sil)
    #cumle
        self.main.pushButton_cumle_sil_geri.clicked.connect(self.c_listele_page)
        self.main.pushButton_cumle_sil.clicked.connect(self.cumle_sil)

    # ayarlar buton
        self.main.pushButton_ayarlar_istatistik_sifirla.clicked.connect(self.oyuncu_ist_sifirla)
        self.main.pushButton_ayarlar_kelime_liste_sil.clicked.connect(self.kelime_liste_sil)
        self.main.pushButton_ayarlar_cumle_liste_sil.clicked.connect(self.cumle_liste_sil)


#########################################################################################################################################################################################



########################### radiobuttonlar ###########################

    # kelime

        self.main.radioButton_kelime_oyun_zor_mod.toggled.connect(self.kelime_oyun_mod_label)
        self.main.radioButton_kelime_oyun_kolay_mod.toggled.connect(self.kelime_oyun_mod_label)

    # cümle
        self.main.radioButton_cumle_oyun_zor_mod.toggled.connect(self.cumle_oyun_mod_label)
        self.main.radioButton_cumle_oyun_kolay_mod.toggled.connect(self.cumle_oyun_mod_label)







##### tabwidget index değişim sinyalleri  ####


#####  listele sayfası
        self.main.tabWidget_listele.currentChanged.connect(self.tab_listele)
        self.main.tabWidget.currentChanged.connect(self.tab_istatistik_ayar)


############################################     stackedwidget currentIndexlerini görüntüleme işlemleri    ##################################################
    # ana 
    def ana_page(self):
        self.main.label_sayfa_ismi.setText("ANA SAYFA")
        self.main.stackedWidget_main.setCurrentIndex(0)
        self.oyun_istatitik()
        self.oyun_ist_goster()
    # oyna
    def oyna_page(self):
        self.main.label_sayfa_ismi.setText("OYNA")

        self.main.stackedWidget_main.setCurrentIndex(1)
    # ekle
    def ekle_page(self):
        self.main.textEdit_cumle_ekle_turkce.clear()
        self.main.textEdit_cumle_ekle_ingilizce.clear()
        self.main.lineEdit_kelime_ekle_ingilizce.clear()
        self.main.lineEdit_kelime_ekle_turkce.clear()
        self.main.label_sayfa_ismi.setText("EKLE")
        if self.main.tabWidget_listele.currentIndex() == 0:
            self.main.stackedWidget_main.setCurrentIndex(2)
            self.main.tabWidget_ekle.setCurrentIndex(0)
        elif self.main.tabWidget_listele.currentIndex() == 1:
            self.main.stackedWidget_main.setCurrentIndex(2)
            self.main.tabWidget_ekle.setCurrentIndex(1)
    # listele
    def c_listele_page(self):
            self.main.label_sayfa_ismi.setText("LİSTELE")
            self.main.stackedWidget_main.setCurrentIndex(3)
            self.main.tabWidget_listele.setCurrentIndex(1)
            self.tum_cumleleri_listele()
    def k_listele_page(self):
            self.main.label_sayfa_ismi.setText("LİSTELE")
            self.main.stackedWidget_main.setCurrentIndex(3)
            self.main.tabWidget_listele.setCurrentIndex(0)
            self.tum_kelimeleri_listele()
    # düzenle
    def duzenle_page(self):
            self.main.lineEdit_duzene_kelime_id.clear()
            self.main.lineEdit_duzenle_kelime_turkce.clear()
            self.main.lineEdit_2_duzenle_kelime_ingilizce.clear()
            self.main.lineEdit_duzenle_cumle_id.clear()
            self.main.textEdit_duzenle_cumle_ingilizce.clear()
            self.main.textEdit_duzenle_turkce.clear()
            self.main.label_sayfa_ismi.setText("DÜZENLE")
            if self.main.tabWidget_listele.currentIndex() == 0:
                self.main.stackedWidget_main.setCurrentIndex(4)
                self.main.tabWidget_duzenle.setCurrentIndex(0)
            elif self.main.tabWidget_listele.currentIndex() == 1:
                self.main.stackedWidget_main.setCurrentIndex(4)
                self.main.tabWidget_duzenle.setCurrentIndex(1)
    # sil
    def sil_page(self):
        self.main.lineEdit_cumle_sil.clear()
        self.main.lineEdit_kelime_sil.clear()
        self.main.label_sayfa_ismi.setText("SİL")
        if self.main.tabWidget_listele.currentIndex() == 0:
            self.main.stackedWidget_main.setCurrentIndex(5)
            self.main.tabWidget_sil.setCurrentIndex(0)
        elif self.main.tabWidget_listele.currentIndex() == 1:
            self.main.stackedWidget_main.setCurrentIndex(5)
            self.main.tabWidget_sil.setCurrentIndex(1)
     
    

#########################################################################################################################################################################################


####  STACKEDWİDGET SAYFALARI

#####################################      anasayfa      #####################################  

##############       Qwidget sayfası için kodlar    ##############

    # kullanici bilgileri düzenleme profil sayfayı açar işlemler yapıldıktan sonra kapatır
    def kullanici_bilgileri_duzenle(self):
        self.kullanici_bilgi.show()
        self.kullanici_bilgi.setWindowTitle('KULLANICI BİLGİLERİNİ GÜNCELLE')
        self.kullanici_bilgi.setFixedSize(650,500)
        self.kullanici_bilgi.kapanma_sinyal.connect(self.Qwidget_close)


    # değiştirilen kullanıcı bilgilerini yeniler
    def yeni_kullanici_bilgileri(self):
        T,data = vt_kullanici_bilgisi_var_mı()
        if T:
            guncel_foto = QPixmap(data[0]) # fotoğrafın yolunu pixmap nesnesine dönüştürdük
            self.main.label_anasayfa_kullanici_adi.setText(data[1])
            self.main.label_anasayfa_kullanici_foto.setPixmap(guncel_foto)
        else:
            self.main.statusbar.showMessage("kullanıcı bilgileri yüklenemedi..",3000)

    # kullanıcı bilgilerini günceller
    def Qwidget_close(self,mesaj):
        self.kullanici_bilgi.close()
        self.yeni_kullanici_bilgileri()

        if mesaj:
            self.main.statusbar.showMessage("BİLGİLER GÜNCELLENDİ",3500)



###############   istatistik barları için kodlar ##################

    # progresbar yüzdelerini girmek
    def oyun_istatitik(self):
        data = vt_oyun_veri_cek()

        if data:

            dogru_yuzde = (data[2] / data[1]) * 100.0
            yanlis_yuzde = (data[3] / data[1]) * 100.0

            # en yakın tam sayıya yuvarlar
            dogru_yuzde = round(dogru_yuzde)
            yanlis_yuzde = round(yanlis_yuzde)

        else:
            dogru_yuzde = 0
            yanlis_yuzde = 0
        

        self.main.progressBar_anasayfa_dogru_oran.setValue(int(dogru_yuzde))
        self.main.progressBar_anasayfa_yanlis_oran.setValue(int(yanlis_yuzde))         


########## oyun ist. gösterme ##########


    def oyun_ist_goster(self):
        data = vt_oyun_veri_cek()

        if data:

            oyun_sayisi = str(data[0])
            soru_sayisi = str(data[1])
            dogru_sayisi = str(data[2])
            yanlis_sayisi = str(data[3])


            self.main.label_istatistik_soru_sayisi.setText(soru_sayisi)
            self.main.label_istatistik_dogru_sayisi.setText(dogru_sayisi)
            self.main.label_istatistik_yanlis_sayisi.setText(yanlis_sayisi)
            self.main.label_istatistik_oyun_sayisi.setText(oyun_sayisi)
        else:
            self.main.label_istatistik_soru_sayisi.setText("-----")
            self.main.label_istatistik_dogru_sayisi.setText("-----")
            self.main.label_istatistik_yanlis_sayisi.setText("-----")
            self.main.label_istatistik_oyun_sayisi.setText("-----")





#################### ayarlar  ############


###### oyun ayarları ##########


# oyuncu verilerini siler
    def oyuncu_ist_sifirla(self):
        T = vt_oyun_veri_cek()
        if T:     
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setText("Kullanıcı oyun verilerini Sıfırlamak istiyor musunuz?")
            msg_box.setWindowTitle("Sıfırlama İşlemi")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            # Kullanıcının seçimini alma
            result = msg_box.exec_()
            if result == QMessageBox.Yes:
                T = vt_kullanici_oyun_verileri_silme()
                if T:
                    self.main.statusbar.showMessage("KULLANICI VERİLERİ SIFIRLANDI",4000)
                else:
                    self.main.statusbar.showMessage("HATA OLUŞTU İŞLEM BAŞARISIZ!",4000)
                
            else:
                self.main.statusbar.showMessage("KULLANICI VERİLERİ SIFIRLAMA İŞLEMİ İPTAL EDİLDİ",3000)
        else:
            self.main.statusbar.showMessage("KULLANICI VERİSİ BULUNMUYOR!",4000)





# kelime ve cümleleri siler


### listedeki kelimeleri silme işlemi
    def kelime_liste_sil(self):
        kelime_var_mi = vt_tum_kelimeleri_listele()
        if kelime_var_mi:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setText("Listedeki tüm kelimeleri silmek istiyor musunuz?")
            msg_box.setWindowTitle("Silme İşlemi")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            result = msg_box.exec_()

            if result == QMessageBox.Yes:
                veriler_silindi = vt_tum_kelimeleri_sil()
                if veriler_silindi:
                    self.main.statusbar.showMessage("KELİME LİSTESİ SİLİNDİ",4000)
                else:
                    self.main.statusbar.showMessage("İŞLEM GERÇEKLEŞMEDİ",4000)
            else:
                    self.main.statusbar.showMessage("İŞLEM İPTAL EDİLDİ",4000)

        else:
            self.main.statusbar.showMessage("LİSTEDE SİLİNECEK KELİME YOK",4000)
         


#### listedeki cümleleri silme işlemi

    def cumle_liste_sil(self):
        cumle_var_mi = vt_tum_cumleleri_listele()
        if cumle_var_mi:
                
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setText("Listedeki tüm cümleleri silmek istiyor musunuz?")
            msg_box.setWindowTitle("Silme İşlemi")
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            result = msg_box.exec_()

            if result == QMessageBox.Yes:

                veriler_silindi = vt_tum_cumleleri_sil()
                if veriler_silindi:
                    self.main.statusbar.showMessage("CÜMLE LİSTESİ SİLİNDİ",4000)
                else:
                    self.main.statusbar.showMessage("İŞLEM GERÇEKLEŞMEDİ",4000)
            else:
                    self.main.statusbar.showMessage("İŞLEM İPTAL EDİLDİ",4000)
        else:
            self.main.statusbar.showMessage("LİSTEDE SİLİNECEK CÜMLE YOK",4000)





#####################################      oyna sayfası     #####################################  


##########################  KELİME OYUN #############################

    # vt dan rasgele 1 kelime(ing,tur) seçer ve bir sözlüğe atar
    def kelime_oyun_sorular(self):
        kelime_sozluk ={}
        data = vt_tum_kelimeleri_listele()


        if data:
            kelime = random.choice(data)
            kelime_sozluk[kelime[1]] = kelime[2]

            return kelime_sozluk
        else:
            return []

    # seçilen kelime sözlüğünden rasgele bir çift seçer
    def kelime_secim(self):
        kelime_sozluk = self.kelime_oyun_sorular()
        if kelime_sozluk:
            keys = list(kelime_sozluk.keys())
            if not keys:
                return None
            random_key = random.choice(keys)

            return (random_key, kelime_sozluk[random_key])
        else:
            return ("","")


    # cevaplara göre sonucu yazdırır
    def kelime_oyun_sonuc(self):
            puan = self.kelime_dogru_sayisi * 10
            self.main.label_kelime_oyun_puan_durumu.setText(str(puan))
            T = vt_oyun_veri_ekle(self.kelime_soru_sayisi,self.kelime_dogru_sayisi,self.kelime_yanlis_sayisi)
            
            if T:
                return True
            else:
                return False
            
    # sayac tamsa sonucu kontrol eder ve yazar
    def kelime_oyun_sonuc_kontrol(self):
        if self.kelime_sayac == 10:
            self.main.label_kelime_oyun_ing.setText("------")
            self.main.radioButton_kelime_oyun_kolay_mod.setEnabled(True)
            self.main.radioButton_kelime_oyun_zor_mod.setEnabled(True)
            self.main.pushButton_kelime_oyun_ileri.setEnabled(False)
            self.main.pushButton_kelime_oyun_oyna.setEnabled(True)

            T = self.kelime_oyun_sonuc()
            if T:
                self.main.statusbar.showMessage("TEST BİTTİ",2000)
        else:
            pass
    # hangi seviyede oynadığımızı gösteren label  -- buradan devam label değişimi 
    def kelime_oyun_mod_label(self):
        if self.main.radioButton_kelime_oyun_kolay_mod.isChecked():
            self.main.label_kelime_oyun_soru_info.setText("kolay mod")
        if self.main.radioButton_kelime_oyun_zor_mod.isChecked():
            self.main.label_kelime_oyun_soru_info.setText("zor mod") 

########## 

    # oyuna başlamak için
    def kelime_oyun_oyna_buton(self):
        # labelları temizler, raddiobutonları kapatır, butonların durumunu değiştirir
        self.main.label_kelimoyun_soru_sayisi.setText("----")
        self.main.label_kelme_oyun_dogru_sayisi.setText("----")
        self.main.label_kelime_oyun_yanlis_sayisi.setText("----")
        self.main.label_kelime_oyun_puan_durumu.setText("----")
        self.kelime_soru_sayisi = 0
        self.kelime_dogru_sayisi = 0
        self.kelime_yanlis_sayisi = 0
        self.kelime_sayac = 0

        if self.main.radioButton_kelime_oyun_kolay_mod.isChecked():
            ing, tur = self.kelime_oyun_soru_kolay()
        if self.main.radioButton_kelime_oyun_zor_mod.isChecked():
            ing, tur = self.kelime_oyun_soru_zor()
        
        if ing !="" and tur !="":
            self.main.pushButton_kelime_oyun_ileri.setEnabled(True)
            self.main.pushButton_kelime_oyun_oyna.setEnabled(False)
            self.main.radioButton_kelime_oyun_kolay_mod.setEnabled(False)
            self.main.radioButton_kelime_oyun_zor_mod.setEnabled(False)
        else:
            self.main.pushButton_kelime_oyun_ileri.setEnabled(False)  # İleri butonunu devre dışı bırak
            self.main.pushButton_kelime_oyun_oyna.setEnabled(True)
            self.main.radioButton_kelime_oyun_kolay_mod.setEnabled(True)
            self.main.radioButton_kelime_oyun_zor_mod.setEnabled(True)
            self.main.statusbar.showMessage("HENÜZ LİSTEDE KELİME YOK! -- LİSTEYE BİRKAÇ KELİME EKLEMEYE NE DERSİN :)",4000)

            
       


    # bir sonraki soruyu açar
    def kelime_oyun_ileri_buton(self):
        self.kelime_sayac += 1

        line_tur = self.main.lineEdit_kelime_oyun_turkce.text()


        if line_tur.lower() == self.kelime_tur:
            self.kelime_dogru_sayisi += 1
            self.kelime_soru_sayisi += 1
            self.main.lineEdit_kelime_oyun_turkce.clear()
            self.main.label_kelme_oyun_dogru_sayisi.setText(str(self.kelime_dogru_sayisi))
            self.main.label_kelimoyun_soru_sayisi.setText(str(self.kelime_soru_sayisi)) 


        else:
            self.kelime_yanlis_sayisi += 1
            self.kelime_soru_sayisi +=1
            self.main.lineEdit_kelime_oyun_turkce.clear()
            self.main.label_kelime_oyun_yanlis_sayisi.setText(str(self.kelime_yanlis_sayisi))
            self.main.label_kelimoyun_soru_sayisi.setText(str(self.kelime_soru_sayisi))

        self.kelime_oyun_sonuc_kontrol()

        if self.main.radioButton_kelime_oyun_kolay_mod.isChecked():
            ing, tur = self.kelime_oyun_soru_kolay()
        elif self.main.radioButton_kelime_oyun_zor_mod.isChecked():
            ing, tur = self.kelime_oyun_soru_zor()



    # kelime oyunu sorusunu hazırlar ekrana yazar kolay mod
    def kelime_oyun_soru_kolay(self):
            ing, tur = self.kelime_secim()
            if ing !="" and tur !="":
                    ing = ing.lower()
                    tur = tur.lower()

                    uz = len(ing)

                    yildiz_index = random.randint(0, uz - 1)

                    sorulan_kelime = ing[:yildiz_index] + "*" + ing[yildiz_index+1:]

                    self.main.label_kelime_oyun_ing.setText(sorulan_kelime)

                    self.kelime_tur = tur

                    return ing,tur
            else:
                return "",""
    
    # kelime oyunu sorusunu hazırlar ekrana yazar zor mod
    def kelime_oyun_soru_zor(self):
        ing, tur = self.kelime_secim()
        if ing !="" and tur != "":
            ing = ing.lower()
            tur = tur.lower()

            uz = len(ing)

            yildiz_index_1 = random.randint(0, uz - 1)
            yildiz_index_2 = random.randint(0, uz - 1)

            sorulan_kelime = list(ing)

            sorulan_kelime[yildiz_index_1] = "*"
            sorulan_kelime[yildiz_index_2] = "*"

            sorulan_kelime = "".join(sorulan_kelime)

            self.main.label_kelime_oyun_ing.setText(sorulan_kelime)

            self.kelime_tur = tur

            return ing, tur
        else:
            return "",""




           ########### cümle oyun  ################



    # vt dan rasgele 1 kelime(ing,tur) seçer ve bir sözlüğe atar
    def cumle_oyun_sorular(self):
        cumle_sozluk ={}
        data = vt_tum_cumleleri_listele()

        if data:

            cumle = random.choice(data)
            cumle_sozluk[cumle[1]] = cumle[2]

            return cumle_sozluk
        else:
            return []


    # seçilen kelime sözlüğünden rasgele bir çift seçer
    def cumle_secim(self):
        cumle_sozluk = self.cumle_oyun_sorular()

        if cumle_sozluk:
            keys = list(cumle_sozluk.keys())
            if not keys:
                return None
            random_key = random.choice(keys)

            return (random_key, cumle_sozluk[random_key])
        else:
            return ("","")
    


    # cevaplara göre sonucu yazdırır
    def cumle_oyun_sonuc(self):
            puan = self.kelime_dogru_sayisi * 10
            self.main.label_cumle_oyunu_puan_durumu.setText(str(puan))
            T = vt_oyun_veri_ekle(self.cumle_oyun_soru_sayisi,self.cumle_oyun_dogru_sayisi,self.cumle_oyun_yanlis_sayisi)
            
            if T:
                return True
            else:
                return False    

        
    # sayac tamsa sonucu kontrol eder ve yazar
    def cumle_oyun_sonuc_kontrol(self):
        if self.cumle_sayac == 10:
            self.main.label_cumle_oyun_ing.setText("-----")
            self.main.radioButton_cumle_oyun_zor_mod.setEnabled(True)
            self.main.radioButton_cumle_oyun_kolay_mod.setEnabled(True)
            self.main.pushButton_cumle_oyun_ileri.setEnabled(False)
            self.main.pushButton_cumle_oyun_oyna.setEnabled(True)

            T = self.cumle_oyun_sonuc()
            if T:
                self.main.statusbar.showMessage("TEST BİTTİ",2000)
        else:
            pass


    # hangi seviyede oynadığımızı gösteren label  -- buradan devam label değişimi 
    def cumle_oyun_mod_label(self):
        if self.main.radioButton_cumle_oyun_kolay_mod.isChecked():
            self.main.label_cumle_oyun_soru_info.setText("kolay mod")
        if self.main.radioButton_cumle_oyun_zor_mod.isChecked():
            self.main.label_cumle_oyun_soru_info.setText("zor mod") 

#########
    # oyuna başlamak için
    def cumle_oyun_oyna_buton(self):
        # labelları temizler, raddiobutonları kapatır, butonların durumunu değiştirir
        self.main.label_cumle_oyunu_soru_sayisi.setText("----")
        self.main.label_cumle_oyunu_dogru_sayisi.setText("----")
        self.main.label_cumle_oyunu_yanlis_sayisi.setText("----")
        self.main.label_cumle_oyunu_puan_durumu.setText("----")
        self.cumle_oyun_soru_sayisi = 0
        self.cumle_oyun_dogru_sayisi = 0
        self.cumle_oyun_yanlis_sayisi = 0
        self.cumle_sayac = 0
        # oyun moduna göre soru çeker
        if self.main.radioButton_cumle_oyun_kolay_mod.isChecked():
            ing, tur = self.cumle_oyun_soru_kolay()
        if self.main.radioButton_cumle_oyun_zor_mod.isChecked():
             ing, tur = self.cumle_oyun_soru_zor()

        if ing !="" and tur !="":
                
            self.main.radioButton_cumle_oyun_zor_mod.setEnabled(False)
            self.main.radioButton_cumle_oyun_kolay_mod.setEnabled(False)
            self.main.pushButton_cumle_oyun_ileri.setEnabled(True)
            self.main.pushButton_cumle_oyun_oyna.setEnabled(False)
        else:                
            self.main.radioButton_cumle_oyun_zor_mod.setEnabled(True)
            self.main.radioButton_cumle_oyun_kolay_mod.setEnabled(True)
            self.main.pushButton_cumle_oyun_ileri.setEnabled(False)
            self.main.pushButton_cumle_oyun_oyna.setEnabled(True)
            self.main.statusbar.showMessage("HENÜZ LİSTEDE CÜMLE YOK! -- LİSTENE BİRKAÇ CÜMLE EKLEMEYE NE DERSİN :)",4000)




    def cumle_oyun_ileri_buton(self):
        self.cumle_sayac += 1

        line_tur = self.main.textEdit_umle_oyun_tur.toPlainText()

        if line_tur.lower() == self.cumle_tur:
            self.cumle_oyun_dogru_sayisi += 1
            self.cumle_oyun_soru_sayisi += 1
            self.main.textEdit_umle_oyun_tur.clear()
            self.main.label_cumle_oyunu_dogru_sayisi.setText(str(self.cumle_oyun_dogru_sayisi))
            self.main.label_cumle_oyunu_soru_sayisi.setText(str(self.cumle_oyun_soru_sayisi))
    
        else:
            self.cumle_oyun_yanlis_sayisi += 1
            self.cumle_oyun_soru_sayisi += 1
            self.main.textEdit_umle_oyun_tur.clear()
            self.main.label_cumle_oyunu_yanlis_sayisi.setText(str(self.cumle_oyun_yanlis_sayisi))
            self.main.label_cumle_oyunu_soru_sayisi.setText(str(self.cumle_oyun_soru_sayisi))
            
            self.cumle_oyun_sonuc_kontrol()

        # oyun moduna göre soru çeker
        if self.main.radioButton_cumle_oyun_kolay_mod.isChecked():
            ing, tur = self.cumle_oyun_soru_kolay()
        elif self.main.radioButton_cumle_oyun_zor_mod.isChecked():
            ing, tur = self.cumle_oyun_soru_zor()




    # kelime oyunu sorusunu hazırlar ekrana yazar kolay mod
    def cumle_oyun_soru_kolay(self):
                ing, tur = self.cumle_secim()
                if ing !="" and tur != "":
                    ing = ing.lower()
                    tur = tur.lower()

                    uz = len(ing)

                    yildiz_index = random.randint(0, uz - 1)

                    sorulan_cumle = ing[:yildiz_index] + "*" + ing[yildiz_index+1:]

                    self.main.label_cumle_oyun_ing.setText(sorulan_cumle)

                    self.cumle_tur = tur

                    return ing,tur
                else:
                    return "",""

    # kelime oyunu sorusunu hazırlar ekrana yazar zor mod
    def cumle_oyun_soru_zor(self):
        ing, tur = self.cumle_secim()
        if ing !="" and tur !="":
            ing = ing.lower()
            tur = tur.lower()

            uz = len(ing)

            yildiz_index_1 = random.randint(0, uz - 1)
            yildiz_index_2 = random.randint(0, uz - 1)
            yildiz_index_3 = random.randint(0, uz -1)

            sorulan_cumle = list(ing)

            sorulan_cumle[yildiz_index_1] = "*"
            sorulan_cumle[yildiz_index_2] = "*"
            sorulan_cumle[yildiz_index_3] = "*"

            sorulan_cumle = "".join(sorulan_cumle)

            self.main.label_cumle_oyun_ing.setText(sorulan_cumle)

            self.cumle_tur = tur

            return ing, tur
        else:
            return "",""




#####################################      ekle sayfası     #####################################  

###################   kelime ekleme

    # ekleme yaptıktan sonra textleri temizler
    def kelime_sayfası_text_temizleme(self):
        self.main.lineEdit_kelime_ekle_ingilizce.clear()
        self.main.lineEdit_kelime_ekle_turkce.clear()


    # veriyi db e işler
    def kelime_ekle(self):
        en = self.main.lineEdit_kelime_ekle_ingilizce.text()
        tr = self.main.lineEdit_kelime_ekle_turkce.text()

        kelime_var = vt_kelime_var_mi(en)

        if kelime_var:
            self.main.statusbar.showMessage("BU  KELİME LİSTEDE VAR",3000)
            self.kelime_sayfası_text_temizleme()
        else:
            T = vt_kelime_ekle(en,tr)
            
            if T:
                self.main.statusbar.showMessage("KELİME EKLENDİ",3000)
                self.kelime_sayfası_text_temizleme()
            else:
                if en =="" or tr == "":
                    self.main.statusbar.showMessage("KELİME EKLEME BAŞARISIZ BİLGİLERİ TAM GİRİNİZ !",3000)
                    self.kelime_sayfası_text_temizleme()



####################### cümle ekleme

    # ekleme yaptıktan sonra textleri temizler
    def cumle_sayfası_text_temizleme(self):
        self.main.textEdit_cumle_ekle_turkce.clear()
        self.main.textEdit_cumle_ekle_ingilizce.clear()

    
    def cumle_ekle(self):
        en = self.main.textEdit_cumle_ekle_ingilizce.toPlainText()
        tr = self.main.textEdit_cumle_ekle_turkce.toPlainText()

        if en != "" or tr != "":
            cumle_var = vt_cumle_var_mi(en)
            if cumle_var:
                self.main.statusbar.showMessage("BU CÜMLE LİSTEDE VAR")
                self.cumle_sayfası_text_temizleme()
            else:
                T = vt_cumle_ekle(en,tr)
                if T:
                    self.main.statusbar.showMessage("CÜMLE EKLENDİ",3000)
                    self.cumle_sayfası_text_temizleme()
                else:
                    self.main.statusbar.showMessage("CÜMLE EKLEME BAŞARISIZ",3000)
                    self.cumle_sayfası_text_temizleme()
        else:
             self.main.statusbar.showMessage("BİLGİLERİ TAM GİRİNİZ !",3000)



#####################################      listele sayfası     #####################################  

                            ############### kelimeler  #################

    # tüm kelimeleri listele
    def tum_kelimeleri_listele(self):
        self.main.lineEdit_listele_ara.clear()
        self.main.tableWidget_listele_kelimeler.clear()
        self.main.tableWidget_listele_kelimeler.setColumnCount(3)  # Sütun sayısını belirle

        # Sütun başlıklarını ayarla
        self.main.tableWidget_listele_kelimeler.setHorizontalHeaderLabels(["ID", "İngilizce", "Türkçe"])

        # Sütun genişliklerini ayarla
        self.main.tableWidget_listele_kelimeler.setColumnWidth(0, 50)
        self.main.tableWidget_listele_kelimeler.setColumnWidth(1, 200)
        self.main.tableWidget_listele_kelimeler.setColumnWidth(2, 200)

        # Listelenecek ürünler fazlaysa onları sıkıştırıp ekrana sığdır
        self.main.tableWidget_listele_kelimeler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Tüm kelimeleri veritabanından çek
        data = vt_tum_kelimeleri_listele()

        # Tablonun satır sayısını ayarla
        self.main.tableWidget_listele_kelimeler.setRowCount(len(data))

        # Tabloya verileri ekle
        for indexSatir, kayitNumarasi in enumerate(data):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.main.tableWidget_listele_kelimeler.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

#######  filtreleyerek 

    # arama sonucuna göre listele
    def aranan_kelimeyi_listele(self):
        self.main.tableWidget_listele_kelimeler.clear()
        self.main.tableWidget_listele_kelimeler.setColumnCount(3)  # Sütun sayısını belirle

        # Sütun başlıklarını ayarla
        self.main.tableWidget_listele_kelimeler.setHorizontalHeaderLabels(["ID", "İngilizce", "Türkçe"])

        # Sütun genişliklerini ayarla
        self.main.tableWidget_listele_kelimeler.setColumnWidth(0, 50)
        self.main.tableWidget_listele_kelimeler.setColumnWidth(1, 200)
        self.main.tableWidget_listele_kelimeler.setColumnWidth(2, 200)

        # Listelenecek ürünler fazlaysa onları sıkıştırıp ekrana sığdır
        self.main.tableWidget_listele_kelimeler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # aranan kelimeyi  veritabanından çek
        kelime = self.main.lineEdit_listele_ara.text()
        if kelime !="":
            data = vt_aranan_kelime_listele(kelime)
            # Tablonun satır sayısını ayarla
            self.main.tableWidget_listele_kelimeler.setRowCount(len(data))

            # Tabloya verileri ekle
            for indexSatir, kayitNumarasi in enumerate(data):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.main.tableWidget_listele_kelimeler.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
        else:
            # self.main.statusbar.showMessage("KELİMEYİ GİRİNİZ!",3000)
            self.tum_kelimeleri_listele()


                            ############### cümleler  #################


    def tum_cumleleri_listele(self):
        self.main.lineEdit_listele_ara.clear()
        self.main.tableWidget_cumleler.clear()
        self.main.tableWidget_cumleler.setColumnCount(3)  # Sütun sayısını belirle

        # Sütun başlıklarını ayarla
        self.main.tableWidget_listele_kelimeler.setHorizontalHeaderLabels(["ID", "İngilizce", "Türkçe"])

        # Sütun genişliklerini ayarla
        self.main.tableWidget_cumleler.setColumnWidth(0, 50)
        self.main.tableWidget_cumleler.setColumnWidth(1, 200)
        self.main.tableWidget_cumleler.setColumnWidth(2, 200)

        # Listelenecek ürünler fazlaysa onları sıkıştırıp ekrana sığdır
        self.main.tableWidget_cumleler.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Tüm kelimeleri veritabanından çek
        data = vt_tum_cumleleri_listele()

        # Tablonun satır sayısını ayarla
        self.main.tableWidget_cumleler.setRowCount(len(data))

        # Tabloya verileri ekle
        for indexSatir, kayitNumarasi in enumerate(data):
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.main.tableWidget_cumleler.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))




#####################################      duzenle sayfası     #####################################  


#############    kelime 
    def kelime_duzenle_text_temizle(self):
        self.main.lineEdit_duzenle_kelime_turkce.clear()
        self.main.lineEdit_2_duzenle_kelime_ingilizce.clear()
        self.main.lineEdit_duzene_kelime_id.clear()

    def kelime_duzenle(self):
        id =  self.main.lineEdit_duzene_kelime_id.text()
        en = self.main.lineEdit_2_duzenle_kelime_ingilizce.text()
        tr = self.main.lineEdit_duzenle_kelime_turkce.text()

        T = vt_kelime_duzenle(id,en,tr)

        if T:
            self.main.statusbar.showMessage("KELİME GÜNCELLENDİ",3000)
            self.kelime_duzenle_text_temizle()
        else:
            if id == "" or en =="" or tr == "":
                self.main.statusbar.showMessage("BİLGİLERİ TAM GİRİNİZ!",3000)
                self.kelime_duzenle_text_temizle()
            else:
                self.main.statusbar.showMessage("BU KELİME MEVCUT DEĞİL !",3000)
                self.kelime_duzenle_text_temizle()


################    cümle  

    def cumle_duzenle_text_temizle(self):
        self.main.lineEdit_duzenle_cumle_id.clear()
        self.main.textEdit_duzenle_cumle_ingilizce.clear()
        self.main.textEdit_duzenle_turkce.clear()


    def cumle_duzenle(self):
        id = self.main.lineEdit_duzenle_cumle_id.text()
        en = self.main.textEdit_duzenle_cumle_ingilizce.toPlainText()
        tr = self.main.textEdit_duzenle_turkce.toPlainText()  

        T = vt_cumle_duzenle(id,en,tr)

        if T:
            self.main.statusbar.showMessage("CÜMLE GÜNCELLENDİ",3000)
            self.cumle_duzenle_text_temizle()   
        else:
            if id == "" or en =="" or tr == "":
                self.main.statusbar.showMessage("BİLGİLERİ TAM GİRİNİZ!",3000)
            else:
                self.main.statusbar.showMessage("BU CÜMLE MEVCUT DEĞİL !",3000)



#####################################      sil sayfası     #####################################  

# kelime sil
    def kelime_sil(self):
        
        id = self.main.lineEdit_kelime_sil.text()

        if id == "":
            self.main.statusbar.showMessage("HATA! ID değeri boş.")
            return
             
        T = vt_kelime_sil(id)

        if T:
            self.main.statusbar.showMessage("KELİME SİLİNDİ",3000)
            self.main.lineEdit_kelime_sil.clear()
        else:
            self.main.statusbar.showMessage("HATA! İŞLEM GERÇEKLEŞMEDİ",3000)
            self.main.lineEdit_kelime_sil.clear()


# cümle sil 
    def cumle_sil(self):
        id = self.main.lineEdit_cumle_sil.text()
        
        if id == "":
            self.main.statusbar.showMessage("HATA! ID değeri boş.")
            return

        success = vt_cumle_sil(id)

        if success:
            self.main.statusbar.showMessage("CÜMLE SİLİNDİ", 3000)
            self.main.lineEdit_cumle_sil.clear()
        else:
            self.main.statusbar.showMessage("HATA! İŞLEM GERÇEKLEŞMEDİ: ", 3000)
            self.main.lineEdit_cumle_sil.clear()



#########################################################################################################################################################################################


#####  tüm etkinlikleri kapat     ####

    # ana pencere kapanınca diğer eçık pencerelerde kapanır
    def closeEvent(self, event):
        # alt sayfaları kapat
        self.kullanici_bilgi.close()
        # event'i devam ettir
        event.accept()


######################   enter    ##################ß
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.aranan_kelimeyi_listele()



################## tabwidget değişim fonksiyonları   ##################

    # listele
    def tab_listele(self, index):
            if index == 1: 
                self.tum_cumleleri_listele() 
            if index == 0:
                self.tum_kelimeleri_listele() 
    

    # istatistik
    def tab_istatistik_ayar(self, index):
        if index == 0:
            self.oyun_istatitik()
            self.oyun_ist_goster()
        elif index == 1:
            pass

