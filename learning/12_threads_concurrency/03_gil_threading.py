import threading
import time

def brew_chai():
    print(f"Brewing chai...{threading.current_thread().name}")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Chai is ready...{threading.current_thread().name}")

thread1 = threading.Thread(target=brew_chai, name="Thread-1")
thread2 = threading.Thread(target=brew_chai, name="Thread-2")

start_time = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f"All chai is ready! Time taken: {end_time - start_time:.2f} seconds")
