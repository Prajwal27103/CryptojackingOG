import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

# Simulating a CPU-intensive task on all cores
def cpu_intensive_task():
    while True:
        _ = [x**2 for x in range(1000000)]  # CPU load operation

if __name__ == '__main__':
    num_cores = multiprocessing.cpu_count()
    with ProcessPoolExecutor(max_workers=num_cores) as executor:
        # Start a CPU-intensive task on each core
        futures = [executor.submit(cpu_intensive_task) for _ in range(num_cores)]
        for future in futures:
            future.result()  # This will keep tasks running indefinitely

