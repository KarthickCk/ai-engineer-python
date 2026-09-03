from multiprocessing import Process, Queue
import time

def prepare_chai(queue):
    queue.put("MasalaChai is ready!")

queue = Queue()

if __name__ == "__main__":

    process = Process(target=prepare_chai, args=(queue,))
    process.start()
    process.join()
    print(queue.get())  # Output: MasalaChai is ready!