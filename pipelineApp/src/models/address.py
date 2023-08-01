class Address():
    def __init__(self, street, number, city, state, country):
        self._street = street
        self.number = number
        self.city = city
        self.state = state
        self.country = country
    
    
    def to_dict(self):
        return {
            '_street': self._street,
            'number': self.number,
            'city': self.city,
            'state': self.state,
            'country': self.country
        }