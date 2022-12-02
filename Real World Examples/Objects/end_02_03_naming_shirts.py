""" Two Names, One Shirt """

class shirt:

    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True

# create one shirt with two names
red = shirt()
crimson = red

# examine the red/crimson shirt
print(id(red))
print(id(crimson))
print(red.clean)
print(crimson.clean)

# spill juice on the red/crimson shirt
red.make_dirty()
print(red.clean)
print(crimson.clean)

# check that red and crimson are the same shirt
print(red is crimson)

# create a second shirt to be named crimson
crimson = shirt()

# examine both shirts
print(id(red))
print(id(crimson))
print(crimson.clean)
print(red.clean)

# clean the red shirt
red.make_clean()
print(red.clean)
print(crimson.clean)

# check that red and crimson are different shirts
print(red is crimson)

