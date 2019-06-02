#%%
class Birey:

    def __init__(self,isim:str,soyisim:str,tcno:int):
        self.isim = isim
        self.soyisim = soyisim
        self.tcno = tcno

class Calismayan(Birey): # Calismayan class'ı Birey class'ını inherit aldı
    pass                 # Yani Artık Birey class'ının bütün özellikleri bu class için geçerli

class Calisan(Birey):
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,maas:int):
        Birey.__init__(self,isim,soyisim,tcno)   #Birey'in init'inde belirttiğimiz selfleri aldı
        self.idno = idno
        self.maas = maas

class Muhendis(Calisan):
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,maas:int,y_dilleri:tuple,yabanciDiller:tuple,bilinenProgramlar:tuple):
        Calisan.__init__(self,isim,soyisim,tcno,idno,maas)
        self.y_dilleri = y_dilleri
        self.yabanciDiller = yabanciDiller
        self.bilinenProgramlar = bilinenProgramlar

class Muhassebeci(Calisan):
    def __init__(self,isim:str,soyisim:str,tcno:int,idno:int,maas:int,bilinenProgramlar:tuple):
        Calisan.__init__(self,isim,soyisim,tcno,idno,maas)
        self.bilinenProgramlar = bilinenProgramlar

x = Muhendis("Alperen","Ağa",13456,1,8000,("Python",),("İngilizce",),("MC Office",))

y = Muhassebeci("Veli","Yılmaz",654321,2,4500,("CNR"))



































#%%
