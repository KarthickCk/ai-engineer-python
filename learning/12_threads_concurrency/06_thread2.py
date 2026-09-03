import threading
import time

def prepare_chai(type_, wait_time):
    print(f"Preparing {type_} chai...")
    time.sleep(wait_time)
    print(f"{type_} chai is ready.")

t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Green", 3))

start_time = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")