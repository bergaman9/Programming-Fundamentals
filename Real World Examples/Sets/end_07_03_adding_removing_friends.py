""" Adding and Removing Friends from Sets """

# revised set of friends to invite
invite = set(['Nestor', 'Amanda', 'Olivia'])

# invite Verne
print('Verne' in invite)
invite.add('Verne')
print(invite)

# make sure Olivia is invited
invite.add('Olivia')
print(invite)

# remove Nestor from invite set
invite.remove('Nestor')
print(invite)
# invite.remove('Nestor') # will throw an error

# start inviting friends
print(invite.pop())
print(invite.pop())
print(invite.pop())
print(invite.pop()) # will throw an error
