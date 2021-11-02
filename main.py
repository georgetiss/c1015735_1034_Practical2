

class Contact:

    def __init__(self, name, number, address, bday):
        if not isinstance(name, str) and isinstance(number, int) and isinstance(address, str) and isinstance(bday, str):
            raise TypeError("Data types for the inputs are incorrect")
        else:
            self.name = name
            self.number = number
            self.address = address
            self. bday = bday

    def __str__(self):
        return "Contact({},{},{},{})".format(self.name, self.number, self.address, self.bday)

    def remove(self):
        pass

    def edit(self):
        pass

    def all_search(self):
        pass

    def search(self):
        pass
