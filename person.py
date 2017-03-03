class Person(object):
    """ class person """
    def __init__(self, name, category):
        """ initializing person attributes """
        self.name = name
        self.category = category

class Fellow(Person):
    """ class fellow inheriting class person """
    def __init__(self, name, accomodation="N"):
        """ Initializing attributes of parent class """
        super(Fellow, staff).__init__(name, category=fellow)

class Staff(Person):
    """ class staff inheriting class person """
    def __init__(self, name, accomodation="N"):
        """ Initializing attributes of parent class """
        super(Staff, self).__init__(name, category=Staff)