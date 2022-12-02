""" A Functional Breakfast """

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')    

def make_omelette():
    mix_and_cook()
    omelette = 'a tasty omelette'
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake

# make some breakfast
print(make_omelette())
print(make_pancake())
