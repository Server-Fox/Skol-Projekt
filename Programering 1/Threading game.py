import threading
import time
import sys
from decimal import Decimal, ROUND_DOWN
from random import randint



class Worker(threading.Thread):
    def __init__(self, name, terminate_event):
        super().__init__()
        self.name = name
        self.terminate_event = terminate_event

    def run(self):
        print(f"{self.name} started")
        i = 0
        start = time.perf_counter()
        while not self.terminate_event.is_set():
            i += 1
            j = randint(1, 10000)
            print(f"{self.name}:{j}")
            if j == 69:
                slut = time.perf_counter()
                total_tid = (slut - start)
                m, s = divmod(total_tid, 60)
                s = Decimal(str(s)).quantize(Decimal('.1'))
                m = Decimal(str(m)).quantize(Decimal('0'), rounding=ROUND_DOWN)
                print(f'{self.name} genererade {i} nummer. Det tog ', end="")
                print(f'{m:} minuter och {s:0f} sekunder.')
                
                self.terminate_event.set()  # Signal all threads to stop
                break
        
        print(f"{self.name} completed")

def main():
    terminate_event = threading.Event()

    # Create and start threads
    threads = []
    for i in range(1, 5):  # Adjust the number of threads as needed
        thread = Worker(f"Thread-{i}", terminate_event)
        thread.start()
        threads.append(thread)


    print(f"{i} thread(s) have terminated.")

if __name__ == "__main__":
    main()
