import chunk
import random
import heapq
import time
from multiprocessing import Pool

if __name__ == '__main__':
    rand_items = [random.randint(1, 100000) for i in range(100000)]

    copy = rand_items.copy()

    s = time.time()
    copy.sort()
    e = time.time()
    print(f"Function: {e - s}")

    chunk_number = 10000
    chunks = []

    for i in range(chunk_number): 
        start_index = i*(len(rand_items)//chunk_number)
        end_index = start_index +  len(rand_items)//chunk_number
        chunks.append(rand_items[start_index:end_index])

    s = time.time()
    pool = Pool()
    sorted_list = pool.map(sorted,chunks)
    pool.close()
    res = list(heapq.merge(*sorted_list))
    e = time.time()

    print(f"Pool: {e - s}")

