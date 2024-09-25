import time
import sys

def slowPrint(String, delay=0.015):
    for char in String:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()