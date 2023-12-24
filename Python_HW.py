
class Book:
    def __init__(self, cnt):
        self.cnt_words = cnt

    def word_count(self):
        return self.cnt_words


class Article:
    def __init__(self, cnt):
        self.cnt_words = cnt

    def word_count(self):
        return self.cnt_words

book = Book(500)
article = Article(800)

def total_words(*mas):
    res = 0
    for i in mas:
        res += i.word_count()
    print(res)

total_words(book,article)

class Box:
    def __init__(self, l,w,h):
        self.l = l
        self.w = w
        self.h = h

    def volume(self):
        return self.l * self.w * self.h
     

class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h
           
def volume(self):
        return 3.14 * self.r**2 * self.h


box = Box(10,20,15)
cylinder = Cylinder(5,15)

def total_volume(*mas):
    res = 0
    for i in mas:
        res += i.volume()
    print(res)
        
total_volume(box,cylinder)

class Dog:
    def make_sound(self):
        print("Barf")

class Cat:
    def make_sound(self):
        print("Meow")     

class Test:
    pass

dog = Dog()
cat = Cat()
test = Test()

def play_sound(*mas):
    for i in mas:
        if isinstance(i, Dog | Cat):
            i.make_sound()
        else:
            print(f"{i.__class__} doesn't delong Dog or Cat")

play_sound(dog,cat,test)