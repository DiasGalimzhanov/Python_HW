

def logIn():
    while True:
        log = input("Enter login")
        pas = input("Enter password")

        logPas = ["user","qwerty"]
        if log == logPas[0] and pas == logPas[1]: 
            print("Authentication completed")
            break
        else: 
            print("Invalid login or password. Try again")
            continue

def converter():
    valutes = {'USD': 420, 'EUR': 510, 'RUB': 5.8}

    kzt = float(input("Insert amount in KZT: "))
    val_choice = int(input("Choose currency:\n 1 USD\n 2 EUR\n 3 RUB\n"))

    val_keys = list(valutes.keys())
    if val_choice <= 0 or val_choice > len(val_keys):
        print("Invalid currency choice.")
        return

    target_currency = val_keys[val_choice - 1]
    converted = kzt / valutes[target_currency]

    result = f"{converted:.2f} {target_currency}"
    print(result)


#converter()

def spending(s,p,m):
    if s+p<=m:print("Yes")
    else: print("No")

def ticket(num):
    first = [int(num[:3])]
    first = sum(first)
    second = [int(num[3:])]
    second = sum(second)

    if first == second: print("Happy")
    else: print("Not happy")

def match():
    n = input("Enter number")
    cnt = 0
    res = 0
    while cnt<n:
        res += cnt
        cnt+=1
    print(res)

def ladder():
    n = int(input("Enter n<=9: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

#ladder()

def square(n):
    for i in range(1, n + 1):
        if i*i >= n: break
        print(i*i)
square(50)
