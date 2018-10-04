import random as rd

# print('This is ice cream.')

scoops = [1, 2, 3, 20, 40, 100]

weight = 12485.34

# print('My ice cream has %i scoops.'%scoops)

# print('My ice cream weighs %f kg.'%weight)

flavors = ['vanilla', 'chocolate', 'dirt']

size_scoops = {1:'small', 2:'medium', 3:'this is almost enought ice cream'}

print('Shopkeeper: Hello, welcome to my ice cream shop. What can I get for you?')

num_scoops = rd.choice(scoops)
current_flavor = rd.choice(flavors)
print('Patron: I\'d like %i scoops of %s please!'%(num_scoops, current_flavor))

if num_scoops > 3:
    print('Shopkeeper: I\'m sorry, but that\'s way too much!')
else:
    if current_flavor == 'dirt':
        print('Shopkeeper: Get out of town!')
        
    else:
        print('Shopkeeper: Well that\'s a reasonable request. Here you go! That will cost $%.2f'%(num_scoops*1.5))
        
        print('Patron: Here you are, thank you!')