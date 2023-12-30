
class Device:
  def __init__(self,name):
    self.name = name
    self.is_work = False

  def turn_on(self):
    self.is_work = True
    print(f"{self.name} is working")

  def turn_off(self):
    self.is_work = False
    print(f"{self.name} doesn't working")

class CoffeeMachine(Device):
  def __init__(self,name):
    super().__init__(name)

  def pour_coffe(self):
    print("Coffe is poured")


class Blender(Device):
  def __init__(self,name):
    super().__init__(name)

  def blend(self):
    print("Blender is blending")


class MeatGrinder(Device):
  def __init__(self,name):
    super().__init__(name)

  def grind(self):
    print("Meat is grinded")


coffe = CoffeeMachine("Coffe machine")
coffe.turn_on()
coffe.pour_coffe()
coffe.turn_off()

class Whell:
  def __init__(self, radius):
    self.radius = radius
    self.is_spinning = False

  def spinning(self):
    self.is_spinning = True
    print("Car rides")


class Engine:
  def __init__(self, volume):
    self.volume = volume
    self.is_start = False

  def start(self):
    self.is_start = True
    print("Sngine start")


class Doors:
  def __init__(self, quantity):
    self.quantity = quantity
    self.is_open = False

  def open(self):
    self.is_open = True
    print("Door is opens")


class Automoblie(Whell, Engine, Doors):
  def __init__(self,name, radius, volume,quantity):
    Whell.__init__(self, radius)
    Engine.__init__(self, volume)
    Doors.__init__(self, quantity)
    self.name = name

  def __str__(self):
    return f"Name: {self.name} \nRadius: {self.radius}\nVolume: {self.volume} \nQuantity: {self.quantity}"

auto = Automoblie("Priora",17, 2.0, 5)
print(auto)
auto.open()
auto.start()
auto.spinning()


class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def Show(self):
       print(f"Coordonats: {self.x}, {self.y}")
   
    def Save(self):
        with open("shape.txt","w") as w_file:
            w_file.write(f"{self.x} {self.y}")
            
    def Load(self):
        with open("shape.txt","r") as r_file:
            content = r_file.readline()
            self.x, self.y = map(int, content.split())
    
    
class Square(Shape):
    def __init__(self, x, y, lng):
        super().__init__(x,y)
        self.lng = lng
        
    def Show(self):
        super().Show()
        print(f"Side: {self.lng}")
        
    def Save(self):
        with open("Square.txt","w") as w_file:
            w_file.write(f"{self.x} {self.y} {self.lng}")
            
    def Load(self):
        with open("Square.txt","r") as r_file:
            content = r_file.readline()
            self.x, self.y, self.lng = map(int, content.split())
            
class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x,y)
        self.a = a
        self.b = b
        
    def Show(self):
        super().Show()
        print(f"Lengh: {self.a} \nWidth: {self.b}")
        
    def Save(self):
        with open("Rectangle.txt","w") as w_file:
            w_file.write(f"{self.x} {self.y} {self.a} {self.b}")
            
    def Load(self):
        with open("Rectangle.txt","r") as r_file:
            content = r_file.readline()
            self.x, self.y, self.a, self.b = map(int, content.split())
            
class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x,y)
        self.r = r
        
    def Show(self):
        super().Show()
        print(f"Radius: {self.r}")
        
    def Save(self):
        with open("Circle.txt","w") as w_file:
            w_file.write(f"{self.x} {self.y} {self.r}")
            
    def Load(self):
        with open("Circle.txt","r") as r_file:
            content = r_file.readline()
            self.x, self.y, self.r = map(int, content.split())
            
class Ellipse(Shape):
    def __init__(self, x, y, a_axis, b_axis,lengh,width):
        super().__init__(x,y)
        self.a_axis = a_axis
        self.b_axis = b_axis
        self.lengh = lengh
        self.width = width
        
    def Show(self):
        super().Show()
        print(f"A axis: {self.a_axis} \nB axis: {self.b_axis} \nLengh: {self.lengh} \nWidth: {self.width}")
        
    def Save(self):
        with open("Ellipse.txt","w") as w_file:
            w_file.write(f"{self.x} {self.y} {self.a_axis} {self.b_axis} {self.lengh} {self.width}")
            
    def Load(self):
        with open("Ellipse.txt","r") as r_file:
            content = r_file.readline()
            self.x, self.y, self.a_axis,self.b_axis,self.lengh,self.width = map(int, content.split())
            
square = Square(2,2,4)
rectangle = Rectangle(4,4,5,6)
circle = Circle(0,0,2)
ellipse = Ellipse(-3,4,3,4,6,8)

mas = [square,square,circle,ellipse]

for i in mas:
    i.Save()
    i.Load()
    i.Show()
