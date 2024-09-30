import threading
import time

def timer_function():
    print("Timer expired!")

def main():
    # Set up the timer to expire after 5 seconds
    timer = threading.Timer(5.0, timer_function)
    
    print("Starting timer...")
    timer.start()  # Start the timer
    
    # Continue with other operations
    for i in range(10):
        print(f"Main thread: {i}")
        time.sleep(1)
    
    print("Main program finished")

if __name__ == "__main__":
    main()
