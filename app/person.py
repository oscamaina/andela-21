class Person(object):
    """ class person """
    def __init__(self, first_name, last_name, category = 'none'):
        """ initializing person attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.category = category

class Fellow(Person):
    """ class fellow inheriting class person """
    def __init__(self, first_name, last_name, accomodation="N"):
        """ Initializing attributes of parent class """
        super(Fellow, self).__init__(first_name, last_name)
        self.category = 'fellow'
        self.accomodation = accomodation

class Staff(Person):
    """ class staff inheriting class person """
    def __init__(self, first_name, last_name):
        """ Initializing attributes of parent class """
        super(Staff, self).__init__(first_name, last_name)
        self.category = 'staff'
