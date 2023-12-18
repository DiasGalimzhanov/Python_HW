
def gen_dictionary(lst):
    return {i:i**3 for i in lst if i%2!=0}

print(gen_dictionary([1,2,3,4,5,6,7]))

def gen_even(lst):
    res = list(dict.fromkeys(lst))
    return {i for i in res if i%2==0 }

print(gen_even([1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]))

def gen_ten():
    for i in range(10):
        yield i * 10

for i in gen_ten():
    print(i)

def gen_seven(n):
    #for i in range(6,n,7): 
    for i in range(n):
        if i % 7 == 0: 
            yield i

for i in gen_seven(70):
    print(i)