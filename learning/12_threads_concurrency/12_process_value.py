from multiprocessing import Process, Value
import time

def prepare_chai(counter):
    for i in range(100000):
        with counter.get_lock():  # Synchronize access to the shared value
            counter.value += 1  # Update the shared value


if __name__ == "__main__":

    counter = Value('i', 0)  # 'i' is for integer, initial value is 0
    processes = [Process(target=prepare_chai, args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(counter.value)