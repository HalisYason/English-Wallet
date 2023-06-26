

#  ENGLİSH WALLET DATABASE CODE



import sqlite3 as sql
import random
import sys


########################################   kullanıcı bilgileri ile ilgili kodlar    ########################################

############### tablo oluşturma

vt = sql.connect("app_data.db")

cursor  = vt.cursor()
cursor.execute("""create table if not exists kullanici_bilgi (
profil_foto blob,
kullanici_adi text

)""")

vt.commit()
vt.close()


##############################   kullanıcı ekler
def vt_kullanici_bilgi_ekle(resim_yolu,ad):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        cursor.execute("insert into kullanici_bilgi values(?,?)",(resim_yolu,ad))

        vt.commit()
        return True


############################  kullanıcı bilgilerini günceller
def vt_kullanici_bilgi_guncelle(resim_yolu, ad):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        if resim_yolu != "" and ad != "":
            cursor.execute("UPDATE kullanici_bilgi SET profil_foto=?, kullanici_adi=? WHERE rowid=1", (resim_yolu, ad))
            vt.commit()
            return True
        elif resim_yolu != "" and ad =="":
            cursor.execute("UPDATE kullanici_bilgi SET profil_foto=? WHERE rowid=1", (resim_yolu,))
            vt.commit()
            return True
        elif resim_yolu =="" and ad !="":
            cursor.execute("UPDATE kullanici_bilgi SET kullanici_adi=?  WHERE rowid=1", (ad,))
            vt.commit()
            return True
        else:
            return False


###############  db de kullanıcı verisi var mı yok mu ona bakar varsa datayı çeker
def vt_kullanici_bilgisi_var_mı():
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        cursor.execute("select * from kullanici_bilgi")

        data =  cursor.fetchone()
        
        if data:
            return (True,data)
        else:
            return (False,data)

       
########################################         kelimeler         ######################################## 


############## tablo oluşturma
vt = sql.connect("app_data.db")
cursor  = vt.cursor()
cursor.execute("""create table if not exists kelimeler (

id text,
ing text,
tur text
)""")

vt.commit()
vt.close()


########### kelime sorgu  -> güncellenmek istenen kelime vt de var mı ona bakar 

def vt_kelime_sorgu(id):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        cursor.execute(f"select * from kelimeler where id='{id}' ")

        data = cursor.fetchall()

        if data == None or data == []:
            return False
        else:
            return True
        
# bir kelimeyi tekrar girmemek için kontrol eder      
def vt_kelime_var_mi(ing):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        cursor.execute(f"select * from kelimeler where ing='{ing}' ")

        data = cursor.fetchall()

        if data == None or data == []:
            return False
        else:
            return True  

############  kelime ekleme
def vt_kelime_ekle(en,tr):
    import random

    id = random.randint(0,100000)
    id  = str(id)


    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        if en != "" and tr != "":
            cursor.execute("insert into kelimeler values(?,?,?)",(id,en,tr))
            vt.commit()
            return True
        else:
            return False

################ kelime   düzenleme

def vt_kelime_duzenle(id,en,tr):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        T = vt_kelime_sorgu(id)
        
        if T:
            if id != "" and en != "" and tr != "":
                cursor.execute(f"update kelimeler set ing = '{en}', tur = '{tr}' where id='{id}' ")
                vt.commit()
                return True
            else:
                return False
        else:
            return False
        

##################### tüm kelimeleri listele


def vt_tum_kelimeleri_listele():
    try:
        with sql.connect("app_data.db") as vt:
            cursor = vt.cursor()
            cursor.execute("SELECT * FROM kelimeler")
            data = cursor.fetchall()
            return data
    except Exception as e:
        return []



#################### ing  aramaya göre listeleme
def vt_aranan_kelime_listele(kelime):
    kelime = kelime.lower()
    try:
        with sql.connect("app_data.db") as vt:
            cursor = vt.cursor()
            cursor.execute("SELECT * FROM kelimeler WHERE LOWER(ing) = LOWER(?)", (kelime,))
            data = cursor.fetchall()
            return data
    except Exception as e:
        return []


################### kelime sil

def vt_kelime_sil(id):

    T = vt_kelime_sorgu(id)

    if T:
        try:
            with sql.connect("app_data.db") as vt:
                cursor = vt.cursor()
                # SQL sorgusunu oluştur ve yürüt
                sorgu = "DELETE FROM kelimeler WHERE id = ?"
                cursor.execute(sorgu, (id,))
                return True
        except Exception as e:
            return False
    else:
        return False
    
############## tüm kelimeleri sil

def vt_tum_kelimeleri_sil():
    try:
        with sql.connect("app_data.db") as vt:
            cursor = vt.cursor()

            cursor.execute("delete from kelimeler")
            vt.commit()
            return True
    except sql.Error:
        return False


# import pandas as pd

# df = pd.read_excel('ttt/Words.xlsx')
# word_list = df.values.tolist()


# cum = pd.read_excel('ttt/cümleler.xlsx')
# cumle_list = cum.values.tolist()






########################################         cümleler         ########################################

############### tablo oluşturma

vt = sql.connect("app_data.db")

cursor  = vt.cursor()

cursor.execute("""create table if not exists cumleler (

id text,
ing text,
tur text
)""")

vt.commit()
vt.close()


# cümle sorgu -> güncellenmek istenen cümle vt de var mı ona bakar 
def vt_cumle_sorgu(id):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        cursor.execute(f"select * from cumleler where id='{id}' ")

        data = cursor.fetchone()

        if data == None or data == ():
            return False
        else:
            return True

# bir cumleyi tekrar girmemek için kontrol eder      
def vt_cumle_var_mi(ing):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        cursor.execute(f"select * from cumleler where ing='{ing}' ")

        data = cursor.fetchall()

        if data == None or data == []:
            return False
        else:
            return True 


##############  cümle ekleme
def vt_cumle_ekle(en,tr):
    import random
    import time
    
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        # her cümle için id üretir
        id = str(random.randint(0, 100000))
        if en !="" and tr !="":
            try:
                cursor.execute('INSERT INTO cumleler VALUES (?,?,?)', (id, en, tr))
                vt.commit()
                return True
            except:
                return False
        else:
            return False


#############   cümle düzenle 
def vt_cumle_duzenle(id,en,tr):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()

        T = vt_cumle_sorgu(id)
        
        if T:
            if id != "" and en != "" and tr != "":
                cursor.execute(f"update cumleler set ing = '{en}', tur = '{tr}' where id='{id}' ")
                vt.commit()
                return True
            else:
                return False
        else:
            return False


################# cümle listele

def vt_tum_cumleleri_listele():    
    try:
        with sql.connect("app_data.db") as vt:
            cursor = vt.cursor()
            cursor.execute("SELECT * FROM cumleler")
            data = cursor.fetchall()
            return data
    except Exception as e:
        return []


################### cumle sil   -- hatalı

def vt_cumle_sil(id):
    try:
        with sql.connect("app_data.db") as vt:
            cursor = vt.cursor()

            cursor.execute("SELECT * FROM cumleler WHERE id = ?", (id,))
            cümle = cursor.fetchone()

            if cümle:
                cursor.execute("DELETE FROM cumleler WHERE id = ?", (id,))
                vt.commit()
                return True
            else:
                return False
    except sql.Error as e:
        return False


############## tüm cümleleri sil

def vt_tum_cumleleri_sil():
    try:
        with sql.connect("app_data.db") as vt:
            cursor = vt.cursor()

            cursor.execute("delete from cumleler")
            vt.commit()
            return True
    except sql.Error:
        return False

########################################         oyun istatistik         ########################################


# kelime oyun

# tablo
vt = sql.connect("app_data.db")

cursor  = vt.cursor()

cursor.execute("""create table if not exists veriler (

oyun_sayisi integer,
soru_sayisi integer,
dogru_sayisi integer,
yanlis_sayisi integer

)""")

vt.commit()
vt.close()


# Veri tabanında veri varsa True döndürür, yoksa False döndürür.
def vt__oyun_veri_var_mi():
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()
        try:
            cursor.execute('SELECT * FROM veriler')
            data = cursor.fetchall()
            if data:
                return True
            else:
                return False
        except:
            return False

# Veri tabanındaki verileri günceller
def vt__oyun_veri_guncelle(dogru, yanlis):
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()
        try:
            cursor.execute(f"""UPDATE veriler SET oyun_sayisi = oyun_sayisi + 1, 
                           soru_sayisi = soru_sayisi + 10, dogru_sayisi = dogru_sayisi + {dogru}, 
                           yanlis_sayisi = yanlis_sayisi + {yanlis} WHERE rowid = 1""")
            
            vt.commit()
            return True
        except:
            return False



# Veri tabanına oyun verisi ekler
def vt_oyun_veri_ekle(soru_s, dogru, yanlis):
    if vt__oyun_veri_var_mi():
        vt__oyun_veri_guncelle(dogru, yanlis)
    else:
        with sql.connect("app_data.db") as vt:
            cursor = vt.cursor()
            try:
                cursor.execute("INSERT INTO veriler VALUES (?, ?, ?, ?)", (1, soru_s, dogru, yanlis))
                vt.commit()
                return True
            except:
                return False





#  oyun verisi çeker
def vt_oyun_veri_cek():
    with sql.connect("app_data.db") as vt:
        cursor = vt.cursor()
        try:
                cursor.execute('select * from veriler')
                data = cursor.fetchone()
                return data
        except:
                return []    
        
        
#############################################################################

########  mevcut verileri silme işlemi


# kullanıcı verilerini silme işlemi


def vt_kullanici_oyun_verileri_silme():
    vt = sql.connect("app_data.db")
    cursor = vt.cursor()

    # kelimeler tablosundaki tüm verileri silme
    try:
        cursor.execute("DELETE FROM veriler")
        vt.commit()
        vt.close()
        return True
       
    except:
        vt.close()
        return False
        


