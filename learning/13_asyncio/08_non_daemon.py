import threading
import time

def monitoring_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(1)  # Simulate a delay in checking stock

threading.Thread(target=monitoring_tea_temp).start()

print("Main program is done")