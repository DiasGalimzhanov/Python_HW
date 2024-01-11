#Galimzhanov Dias

import threading
import time

def creater_file(name):
    file = open(f"files\{name}.txt","w")
    file.close()
    time.sleep(1)

def without_delay(name):
    file = open(f"files\{name}.txt","w")
    file.close()

fun_s = time.perf_counter()
[creater_file(i) for i in range(100)]
fun_e = time.perf_counter()

thr_s = time.perf_counter()
threads = [threading.Thread(target = creater_file, args = (i,)) for i in range(100,200)]
[i.start() for i in threads]
[i.join() for i in threads]
thr_e = time.perf_counter()

wd_s = time.perf_counter()
[without_delay(i) for i in range(200,300)]
wd_e = time.perf_counter()

print(f"Time of function: {fun_e - fun_s}")
print(f"Time of threads: {thr_e - thr_s}")
print(f"Time of without delay: {wd_e - wd_s}")
