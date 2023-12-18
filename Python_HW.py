from itertools import cycle,count,starmap,accumulate,dropwhile

def cycle_string(st, n):
    st_cycle = cycle(st)
    res = ''.join(next(st_cycle) for i in range(n * len(st)))
    return res

print(cycle_string("abc", 3))

def count_from(start,n):
    cnt = count(start,1)
    res = [next(cnt) for i in range(n)]
    return res

print(count_from(5,3))

def multiply_elements(lst_cort):
    def mult(x,y):
        return x*y
    res = list(starmap(mult,lst_cort))
    return res

print(multiply_elements([(1, 2), (3, 4), (5, 6)]))

def accumulate_sums(arr):
    def sum(x,y):
        return x + y
    res =  list(accumulate(arr,sum))
    return res

print(accumulate_sums(([1, 2, 3, 4, 5])))

def drop_less_than(lst,n):
    def fun(x):
        return x < n
    res = list(dropwhile(fun,lst))
    return res

print(drop_less_than([1, 2, 3, 4, 5], 3))