import time
from multiprocessing import Pool, cpu_count 

def remove_dublicate():
    return "Bitti."

if __name__ == "__main__":
    pool = Pool(cpu_count())
    start_time = time.perf_counter()
    result = pool.map(remove_dublicate, [()])
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")
