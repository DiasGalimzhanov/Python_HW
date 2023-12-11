

def create_arr():
    while True:
        size = input("Enter size array: ")
        data = input("Enter array (n n n n ....): ")
        arr = data.split()
        arr_int = [int(i) for i in arr]

        if len(arr_int) != int(size):
            print("Size does not match. Try again")
            continue
        else: 
            cnt_even = []
            cnt_odd = []
            for i in arr_int:
                if i%2==0: cnt_even.append(i)
                elif i%2!=0: cnt_odd.append(i)
            print(cnt_even)
            print(cnt_odd)
            print("No" if len(cnt_even)<=len(cnt_odd) else "Yes")
            break

#create_arr()

def diagonal():
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(arr[0][0]+arr[1][1]+arr[2][2])

def fibonacci(n):
    if n == 1: return 0
    elif n == 2: return 1
    else: return fibonacci(n - 1) + fibonacci(n-2)

def fib_print():
    for i in range(1, 10):
        print(f"fibonacci number {i} = {fibonacci(i + 1)}")

#fib_print()
def power_two(n):
    return (n & (n - 1)) == 0

print(power_two(8))