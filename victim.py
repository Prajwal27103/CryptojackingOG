import time

# Simulating a CPU-intensive task
def cpu_intensive_task():
    print("Cryptojacking simulation started...")
    while True:
        _ = [x**2 for x in range(1000000)]  # CPU load operation

cpu_intensive_task()