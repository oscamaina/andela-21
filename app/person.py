class Person(object):
    """ class person """
    def __init__(self, name, category = 'none', id =0):
        """ initializing person attributes """
        self.name = name
        self.category = category
        self.office = ""
        self.living = ""
        self.id = id

class Fellow(Person):
    """ class fellow inheriting class person """
    def __init__(self, name, accomodation="N"):
        """ Initializing attributes of parent class """
        super(Fellow, self).__init__(name)
        self.category = 'fellow'
        self.accomodation = accomodation

class Staff(Person):
    """ class staff inheriting class person """
    def __init__(self, name):
        """ Initializing attributes of parent class """
        super(Staff, self).__init__(name)
        self.category = 'staff'
