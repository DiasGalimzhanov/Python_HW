#Galimzhanov Dias

import threading
import time

def creater_file(name):
    file = open(f"files\{name}.txt","w")
    file.close()
    time.sleep(1)

fun_s = time.perf_counter()
for i in range(100):
    creater_file(i)
fun_e = time.perf_counter()

thr_s = time.perf_counter()
threads = [threading.Thread(target = creater_file, args = (i,)) for i in range(100,200)]
for i in threads:
    i.start()

for i in threads:
    i.join()
thr_e = time.perf_counter()

print(f"Time of function: {fun_e - fun_s}")
print(f"Time of threads: {thr_e - thr_s}")
