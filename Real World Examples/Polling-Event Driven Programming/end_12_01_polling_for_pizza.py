""" Polling for Pizza to Cure My Hunger """

import time

hungry = True; # I need a pizza!

while(hungry):

    print('Opening the front door')
    front_door = open('front_door.txt', 'r')

    if "Pizza Guy" in front_door:
        print("Pizza's here!")
        hungry = False;
    else:
        print("Not yet...")

    print('Closing the front door.')
    front_door.close()

    time.sleep(1) # rest for 1 second
