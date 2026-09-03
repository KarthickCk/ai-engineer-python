from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Brewing chai for {name}")
    time.sleep(3)
    print(f"Chai for {name} is ready!")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Customer #{i}",))
        for i in range(1, 4)
    ]

    # start all processes
    for maker in chai_makers:
        maker.start()
        
    # wait for all processes to complete
    for maker in chai_makers:
        maker.join()

    print("All chai is ready!")