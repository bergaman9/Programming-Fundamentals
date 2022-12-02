""" The Blueprints for Jeans """

class jeans:

    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False
    
    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True


    def take_off(self):
        print('Taking off {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = False
        
# create and examine a pair of jeans
my_jeans = jeans(31,32,'blue')
print(type(my_jeans))
print(dir(my_jeans))

# don and remove the jeans
my_jeans.put_on()
print(my_jeans.wearing)

my_jeans.take_off()
print(my_jeans.wearing)
