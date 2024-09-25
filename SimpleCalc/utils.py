import time
import random
import sys
import threading
import audio

AMBER = '\033[38;2;255;191;0m'
RESET = '\033[0m'


def print_color(text='', color=AMBER,):
    
    for i in (text):
        rand = random.uniform(0.06, 0.1)
        time.sleep(rand)    
        sys.stdout.write(f'{color}{i}')
        if i != ' ':
            threading.Thread(target=audio.play_beep_sound).start()
    
    

    

def loading(duration = random.uniform(1.2, 1.7), repeats = 3 ):
    symbol = '.'
    for i in range(repeats):
        time.sleep(duration)
        print_color('loading' + symbol + '\n') 
        symbol += '.'
        if i == repeats -1:
            time.sleep(3)       

def memcheck():
    time.sleep(1)
    print_color('Memtest...\n')
    time.sleep(2)
    print_color('Memory OK\n')
    time.sleep(1)
