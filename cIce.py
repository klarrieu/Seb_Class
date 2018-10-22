import random as rd
import logging

class Ice:
    '''Can set temperament to polite or rude'''

    def __init__(self, temperament, *args, **kwargs):
        
        self.logger = logging.getLogger('icelog.log')
        self.flavors = ['vanilla', 'chocolate', 'dirt']
        self.desc = {1: 'small', 2: 'medium', 3: 'large', 4: 'extra large', 20: 'family size'}
        self.temperament = temperament

    def get_menu(self):
        # reads ice menu from ice.xlsx
        data_file = cio.Read(  os.path.dirname(__file__) + '\\ice.xlsx', 0, "icelog.log")
        self.flavors = data_file.read_column("B", 3)
        self.logger.info("Menu: \n" + "\n".join(self.flavors))

        ###

        data_file.close_wb()

    def get_size_price(self, scoops):

        size = self.desc[scoops]
        price = (scoops**0.75)*1.5
        return size, price

    def dialogue(self, scoops):

        num_scoops = scoops
        size, price = self.get_size_price(scoops)
        current_flavor = rd.choice(self.flavors)

        self.logger.info('Shopkeeper: Hello, welcome to my ice cream shop. What can I get for you?')
        if self.temperament == 'rude':
            self.logger.info('Patron: Give me %i scoops of %s!' % (num_scoops, current_flavor))
        else:
            self.logger.info('Patron: I\'d like %i scoops of %s please!' % (num_scoops, current_flavor))

        if num_scoops > 4:
            self.logger.info('Shopkeeper: I\'m sorry, but that\'s way too much!')
            if self.temperament == 'polite':
                new_scoops = rd.choice([1, 2, 3])
                new_price = (new_scoops**0.5)*1.5
                self.logger.info('Patron: I understand, well then I\'ll just take %i scoops.' % new_scoops)
                self.logger.info('Shopkeeper: Well that\'s a reasonable request. Here you go! That will cost $%.2f.' % new_price)
                self.logger.info('Patron: Here you are, thank you!')
            elif self.temperament == 'rude':
                self.logger.info('Patron: Well this is a stick-up! Hand over the sweets and nobody gets hurt!')
                self.logger.info('Shopkeeper: Ahhhh!')
                self.logger.info('*Patron grabs the goods and makes a dash.*')
        else:
            if current_flavor == 'dirt':
                self.logger.info('Shopkeeper: Get out of town!')
            else:
                self.logger.info('Shopkeeper: Well that\'s a reasonable request. Here you go! That will cost $%.2f.' % price)
                if self.temperament == 'rude':
                    self.logger.info('*Patron throws a wad of cash across the table.*')
                else:
                    self.logger.info('Patron: Here you are, thank you!')

        self.logger.info('\nFin.\n\n*fade to black*\n')

        return size, '%.2f' % price

    def __call__(self, *args, **kwargs):
        self.dialogue()
