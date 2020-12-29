from sys import exit
import time

try:
    for word in open("dictionary.txt").read().splitlines():
        print(word)
except KeyboardInterrupt:
    print("Exiting..")
    time.sleep(.5)
    exit()
