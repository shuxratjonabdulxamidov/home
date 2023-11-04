class Kampitur:
    def __init__(self,narxi,rangi,nomi, apiratifga,xotra):
        self.narxi=narxi
        self.rangi=rangi
        self.nomi=nomi
        self.aperatifga=apiratifga
        self.xotra=xotra
    def info (self):
        info =f"{self.narxi},{self.rangi}.{self.nomi}.{self.aperatifga}.{self.xotra}"

class Kampyuter(Kampitur):
    def __init__(self,fabrika, hojayini, uymanzili, ):
        super().__init__(self, fabrika, hojayini,uymanzili)

        def fabrika(self):
            return self.fabrika
        
        def hojayini(self):
            return self.hojayini
        
        def uymanzili(self):
            return self.uymanzili
        
    def info(self):
            info=f"{self.fabrika}fabrikasi,{self.hojayini}hojayinning ismi,{self.uymanzili}vodisidan,"  
            return info  

class Malumot:
    def __init__(self,dokonnomi,sotishturi,):
        self.dokonnomi=dokonnomi
        self.sotishturi=sotishturi
            
    def Malumot_info(self):
        info=f"{self.dokonnomi} dokoni,{self.sotishturi}sotiladi,"  
        return info      
            
class Obbo:
    def __init__(self,javobgarlig,mudati,):
          self.javobgarlig=javobgarlig
          self.mudati=mudati
    def info(self):
        info=f"{self.javobgarlig},{self.mudati}"
        return info

nuton=True
while nuton:
    narxi = input('narxini kiriting: ')
    rangi = input("rangini kiriting: ")
    nomi = input("nomini kiritnig: ")
    aperativka = input("aperatifkani kiriting: ")
    xotira = input("xotirasi qancha: ")
    fabrika = input("fabrika nomi nima: ")
    hojayin = input("hojayin ismi nima: ")
    uymanzil = input("uymanzili qayerda: ")
    dokon = input("dokon nomi nima: ")
    sotish = input("sotish turi: ") 
    javob=input("javob berganmi: ")
    mudat=input("mudat qancha: ")

print(Kampitur)    
