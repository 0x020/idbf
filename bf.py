from string import ascii_letters, digits
from itertools import product
from pathlib import Path
from sys import exit
import time

try:
    file = Path('log.txt')

    while True:
        if file.is_file():
            lines = open(file, 'r').readlines()
            break
        else:
            Path('log.txt').touch()

    def password_cracker(correct):

        chars = ascii_letters + digits
        att = 0

        for password_length in range(1, 9):
            for paw in product(chars, repeat=password_length):
                att += 1
                paw = ''.join(paw)
                if paw == correct:
                    with open(file, 'a') as i:
                        i.write(f'Found Password: {paw} Took: {att} attempts \n')
                    return f'Found Password {paw} Took: {att} attempts.'
                print(paw)

    print(password_cracker('byt3'))
except KeyboardInterrupt:
    print("Exiting..")
    time.sleep(.5)
    exit()
