from multiprocessing import Process
import time

def crunch_number():
    print(f"Crunching numbers...{Process().name}")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Done crunching numbers...{Process().name}")

if __name__ == "__main__":
    process1 = Process(target=crunch_number, name="Process-1")
    process2 = Process(target=crunch_number, name="Process-2")

    start_time = time.time()

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()

    print(f"All numbers crunched! Time taken: {end_time - start_time:.2f} seconds")