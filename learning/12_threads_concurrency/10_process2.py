from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**8):
        total += i
    print(f"Done! Total: {total}")

if __name__ == "__main__":

    start_time = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time}")
