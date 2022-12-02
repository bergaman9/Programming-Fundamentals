""" Scrubbing A Stuborn Pan """

import random

dirty = True # state of the pan
scrub_count = 0 # number of scrubs

while(dirty):

    scrub_count += 1
    print('Scrub the pan: {}'.format(scrub_count))
    
    if not random.randint(0,9):
        print('All clean!')
        dirty = False
    else:
        print('Still dirty...')  

    print('Rinse & check if the pan is clean.') 