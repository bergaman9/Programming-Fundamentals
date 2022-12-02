""" I'll Have the Special! """

specials = {'Sunday'    : 'spinach', 
            'Monday'    : 'mushroom', 
            'Tuesday'   : 'pepperoni', 
            'Wednesday' : 'veggie',
            'Thursday'  : 'bbq chicken',
            'Friday'    : 'sausage',
            'Saturday'  : 'Hawaiian'}

def order(day):
    pizza = specials[day]
    print('Order the {} pizza.'.format(pizza))

# order the Saturday special!
order('Saturday')
