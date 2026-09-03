import threading
import time

def boiling_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk is boiled.")

def toasting_bread():
    print(f"Toasting bread...")
    time.sleep(3)
    print(f"Bread is toasted.")

t1 = threading.Thread(target=boiling_milk)
t2 = threading.Thread(target=toasting_bread)

start_time = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")