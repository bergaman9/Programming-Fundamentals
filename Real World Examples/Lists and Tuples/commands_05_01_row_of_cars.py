""" Parking Cars in a List """

# create a list of cars
row = ['Ford','Audi','BMW','Lexus']

# park my Mercedes at the end of the row
row.append('Mercedes')
print(row)
print(row[4])

# swap the BMW at index 2 for a Jeep
row[2] = 'Jeep'
print(row)

# park a Honda at the end of the row
row.append('Honda')
print(row)
print(row[4])

# park a Kia at the front of the row
row.insert(0,'Kia')
print(row)
print(row[4])

# find my Mercedes and leave the list
print(row.index('Mercedes'))
print(row.pop(5))
print(row)

# find and remove the Lexus
row.remove('Lexus')
print(row)
