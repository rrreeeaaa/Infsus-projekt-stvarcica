
from pony.orm import *
from datetime import datetime

db = Database()

class Proizvod(db.Entity):
    id = PrimaryKey(int, auto=True)
    naziv = Required(str)
    cijena = Required(float)
    kolicina = Required(int)
    kategorija = Required(str)
    datum_dodavanja = Required(datetime)
    datum_azuriranja = Required(datetime)
