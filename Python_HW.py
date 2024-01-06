from functools import total_ordering

#Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
#Проверка на равенство радиусов двух окружностей (операция = =);
#Сравнения длин двух окружностей (операции >, <, <=,>=);
#Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).

#@total_ordering
class Circle:
    def __init__(self,r,l):
        self.r = r
        self.l = l

    def __eq__(self, obj):
        return self.r == obj.r

    def __lt__(self, obj):
        return self.l < obj.l

    def __gt__(self, obj):
        return self.l > obj.l

    def __le__(self, obj):
        return self.l >= obj.l

    def __ge__(self, obj):
        return self.l <= obj.l

    #в данном коде + и += вроде не будут отличаться
    def __add__(self, n):
        self.r += n
        return self

    def __sub__(self, n):
        self.r -= n
        return self


#a = Circle(3,6)
#b = Circle(2,4)
#a = a + 3
#print(a.r)
#print(a>b)
#Вам необходимо создать класс Airplane (самолет). 
#С помощью перегрузки операторов реализовать: 
#Проверка на равенство типов самолетов (операция = =); 
#Увеличение и уменьшение пассажиров в салоне самолета (операции +  - +=  -=);
#Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > <  <=  >=).

class Airplance:
    def __init__(self,type,cnt_pass, max_pass):
        self.type = type
        self.cnt_pass = cnt_pass
        self.max_pass = max_pass

    def __eq__(self, obj):
        return self.type == obj.type

    def __add__(self,n):
        self.cnt_pass += n
        return self

    def __sub__(self,n):
        self.cnt_pass -= n
        return self

    def __lt__(self, obj):
        return self.max_pass < obj.max_pass

    def __gt__(self, obj):
        return self.max_pass > obj.max_pass

    def __le__(self, obj):
        return self.max_pass >= obj.max_pass

    def __ge__(self, obj):
        return self.max_pass <= obj.max_pass
    
            
#Создайте класс Roman (РимскоеЧисло), представляющий римское число и поддерживающий операции +, -, *, /.
#При реализации класса:
#операции +, -, *, / реализуйте как специальные методы 
#методы преобразования как статические методы.

class Roman:
    roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 
                     'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    def __init__(self, roman):
        self.roman = roman
        self.n = Roman.to_int(self.roman)
        

    @staticmethod
    def to_roman(n):
        roman = ''
        for letter, value in Roman.roman_numbers.items():
            while n >= value:
                roman += letter
                n -= value
        return roman

    @staticmethod
    def to_int(roman):
        result = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i + 2] in Roman.roman_numbers:
                result += Roman.roman_numbers[roman[i:i + 2]]
                i += 2
            else:
                result += Roman.roman_numbers[roman[i]]
                i += 1
        return result

    def __add__(self,obj):
        self.n += obj.n
        self.roman = Roman.to_roman(self.n)
        return self

    def __sub__(self,obj):
        if self.n > obj.n:
            self.n -= obj.n
            self.roman = Roman.to_roman(self.n)
            return self
        else: 
            self.roman = "I"
            return self

    def __mul__(self,obj):
        self.n = self.n * obj.n
        self.roman = Roman.to_roman(self.n)
        return self

    def __truediv__(self,obj):
        print(self.n , obj.n)
        if self.n > obj.n:
            self.n = self.n / obj.n
            self.roman = Roman.to_roman(int(self.n))
            return self
        else: 
            self.roman = "I"
            return self


d = Roman("V")
e = Roman("LV")
#i = d + e
#print(i.roman)
c = e / d
print(c.roman)



