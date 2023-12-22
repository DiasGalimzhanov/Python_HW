

def plus_two(number):  
    try:   
        print(number + 2)   
    except:        
        print("The expected data type is a number")
        
plus_two("a")


def idx_out():
    mas = [1,5,4,7,9,3]   
    try:       
        for i in len(mas):            
            print(mas[i])   
    except:         
        print("Index out array")
        

idx_out()