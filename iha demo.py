"""
utf = 'eng'
UAV demo program in demo process, intended to be practical about object-oriented programming
Mustafa Kemal University Management Information Systems Seyhmus Gurkan

utf = 'tr'
Obje odaklı programlama ile ilgili pratik olması amaçlanan henüz demo sürecindeki iha demo programı 
Mustafa Kemal Üniversitesi Yönetim Bilişim Sistemleri Şeyhmus Gürkan

"""
import time

class İHA():
    def __init__(self,marka,üretimtarihi,kalkisyeri,hedef,koordinat,ekipman):
        self.marka = marka
        self.üretimtarihi = üretimtarihi
        self.kalkisyeri = kalkisyeri
        self.hedef = hedef
        self.koordinat = koordinat
        self.ekipman = ekipman
    def bilgilerigoster(self):
        print("Bilgiler gösteriliyor...")
        print("""
        
            Marka: {}
            Model: {}
            Üretim Tarihi: {}
            Kalkış Yeri: {}
            Hedef: {}
            Koordinatlar: {}
            Ekipman: {}
        """.format(self.marka,self.üretimtarihi,self.kalkisyeri,self.hedef,self.koordinat,self.ekipman))
    def hedefekle(self,yeni_hedef):
        print("Hedef ekleniyor...")
        time.sleep(1)
        self.hedef.append(yeni_hedef)
    def koordinatekle(self,yeni_koordinat):
        print("Koordinat ekleniyor...")
        time.sleep(1)
        self.koordinat.append(yeni_koordinat)
    def ekipmanekle(self,yeni_ekipman):
        print("Ekipman ekleniyor...")
        time.sleep(1)
        self.ekipman.append(yeni_ekipman)
"""
Örnek kullanım İHA adlı clasımıza obje eklemek ve yazdırmak için:
objeadi = sınıf(DEĞERLER(opsiyonel))
iha1 = İHA("TB2","2018",["Moskova"],["50.3133333°K 30.6833333°D"],["GPS destekli INS özelliği"])

"""
iha1 = İHA("MODEL","2018",["YIL"],["KOORDİNAT GİRİN"],["MODEL GİRİN"])
print(iha1.bilgilerigoster())