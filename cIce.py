import random as rd


class Ice:
    '''Can set temperament to polite or rude'''

    def __init__(self, temperament, *args, **kwargs):
        self.flavors = ['vanilla', 'chocolate', 'dirt']
        self.scoops = [1, 2, 3, 20, 40, 100]
        self.temperament = temperament

    def get_scoops_price(self):
        num_scoops = rd.choice(self.scoops)
        price = (num_scoops**0.5)*1.5

        return num_scoops, price

    def dialogue(self, *args, **kwargs):

        num_scoops, price = self.get_scoops_price()
        current_flavor = rd.choice(self.flavors)

        print('Shopkeeper: Hello, welcome to my ice cream shop. What can I get for you?')
        if self.temperament == 'rude':
            print('Patron: Give me %i scoops of %s!' % (num_scoops, current_flavor))
        else:
            print('Patron: I\'d like %i scoops of %s please!' % (num_scoops, current_flavor))

        if num_scoops > 3:
            print('Shopkeeper: I\'m sorry, but that\'s way too much!')
            if self.temperament == 'polite':
                new_scoops = rd.choice([1, 2, 3])
                new_price = (new_scoops**0.5)*1.5
                print('Patron: I understand, well then I\'ll just take %i scoops.' % new_scoops)
                print('Shopkeeper: Well that\'s a reasonable request. Here you go! That will cost $%.2f.' % new_price)
                print('Patron: Here you are, thank you!')
            elif self.temperament == 'rude':
                print('Patron: Well this is a stick-up! Hand over the sweets and nobody gets hurt!')
                print('Shopkeeper: Ahhhh!')
                print('*Patron grabs the goods and makes a dash.*')
        else:
            if current_flavor == 'dirt':
                print('Shopkeeper: Get out of town!')
            else:
                print('Shopkeeper: Well that\'s a reasonable request. Here you go! That will cost $%.2f.' % price)
                if self.temperament == 'rude':
                    print('*Patron throws a wad of cash across the table.*')
                else:
                    print('Patron: Here you are, thank you!')

        print('\nFin.\n\n*fade to black*')

    def __call__(self, *args, **kwargs):
        self.dialogue()
