class Balik():
    def __init__(self, adresa, hmotnost, doruceno=False):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = doruceno
    
    def deliver(self):
        self.doruceno = True
    
    def __str__(self):
        if self.doruceno:
            return f"Balik s adresou {self.adresa} o hmotnosti {self.hmotnost}kg byl dorucen."
        else:
            return f"Balik s adresou {self.adresa} o hmotnosti {self.hmotnost}kg nebyl dorucen."
    

balik = Balik('Strasnicka 100, Praha 10', 10)
balik.deliver()
print(balik)

class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota, doruceno=False):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = doruceno
        self.hodnota = hodnota

    def __str__(self):
        text = super().__str__()
        text = text + f" Hodnota belíku: {self.hodnota}"
        return text

cennyBalik2 = CennyBalik ('Strasnicka 100, Praha 10', 10, 10)
print(cennyBalik2)