

def IsAscending(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return "NO"        
    return "YES"
        
print(IsAscending([1,7,3,4,5]))

def KthAppearance(A, a, k):
    cnt = 0
    for i in range(len(A)):
        if A[i] == a:
            cnt += 1
            if cnt == k:
                return i  
    return -1

print(KthAppearance([1, 2, 1, 3, 2, 3, 2, 3, 2, 2],3,2))

def archive(s): 
    arr_s = s.split()
    arr_int = [int(i) for i in arr_s]
    all_size = arr_int.pop(0)
    arr_int.pop(0)
    arr_int.sort()
    cnt = 0
    res = 0
    for i in arr_int:
        res += i
        if res <= all_size: cnt+=1
        else: break
    print(cnt)

archive("100 2 100 50")

def taxi(distance,rate):
    d = list(map(int, distance.split()))
    r = list(map(int, rate.split()))
    res = []
    for i in range(len(d)):
        res.append(d[i] * r[i])
    print(sum(res))

taxi("10 20 30","20 30 40")

def count_digits(arr):
    cnt = [0] * 9   
    for i in arr:
        if i == 0: break
        cnt[i - 1] += 1  
    return cnt


print(count_digits([1,2,3,4,5,6,1,1]))