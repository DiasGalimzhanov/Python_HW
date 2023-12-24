
from lib2to3.pgen2 import pgen
from tokenize import ContStr


class Auto():
    def __init__(self, mdl,yr,man,engn,clr,cst):
        self.model = mdl
        self.year = yr
        self.manufacturer = man
        self.engin = engn
        self.color = clr
        self.coast = cst

    def setModel(self, mdl):
        self.model = mdl

    def getModel(self):
        return self.model

    def setYear(self, yr):
        self.year = yr

    def getYear(self):
        return self.year

    def setManufacturer(self, man):
        self.manufacturer = man

    def getManufacturer(self):
        return self.manufacturer

    def setEngin(self, engn):
        self.engin = engn

    def getEngin(self):
        return self.engin

    def setColor(self, clr):
        self.color = clr

    def getColor(self):
        return self.color

    def setCoast(self, cst):
        self.coast = cst

    def getCoast(self):
        return self.coast

    def __str__(self): 
        return f"Model: {self.model} \nYear: {self.year} \nManufacturer: {self.manufacturer} \nEngin: {self.engin} \nColor: {self.color} \nCoast: {self.coast} "


Priora = Auto("Priora", 2011, "Lada", 1.6, "Gray", 4000)
print(Priora)

print("\n--------------------------------------------------------")

class Book():
    def __init__(self, nm, yr, pb, gnr, aut, cst):
        self._name = nm
        self._year = yr
        self._publisher = pb
        self._genre = gnr
        self._author = aut
        self._coast = cst

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, nm):
        self._name = nm

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, yr):
        if yr > 1000:
            self._year = yr
        else: 
            self._year = 1000

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, pb):
        self._publisher = pb

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, gnr):
        self._genre = gnr

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, aut):
        self._author = aut
   
    @property
    def coast(self):
        return self._coast

    @coast.setter
    def coast(self, cst):
        if cst > 0:
            self._coast = cst
        else: 
            self._coast = 0

    def __str__(self):
        return f"Name: {self._name} \nYear: {self._year} \nPublisher: {self._publisher} \nGenre: {self._genre} \nAuthor: {self._author} \nCoast: {self._coast}"

DarkTower = Book("Dark tower", 1982, "AST", "adventure", "Stephen Edwin King", 5000)
print(DarkTower)