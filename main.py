import csv

class Contact:

    def __init__(self, name, number, address, bday):
        if not isinstance(name, str) and isinstance(number, int) and isinstance(address, str) and isinstance(bday, str):
            raise TypeError("Data types for the inputs are incorrect")
        else:
            self.name = name
            self.number = number
            self.address = address
            self. bday = bday

            data = [self.name, self.number, self.address, self.bday]

        with open('contact_data.csv', 'a+', newline='') as savecsv:
            #code adapted from https://www.pythontutorial.net/python-basics/python-write-csv-file/#:~:text=%20To%20write%20data%20into%20a%20CSV%20file%2C,you%20complete%20writing%20data%20to%20it.%20More%20
            data_writer = csv.writer(savecsv)
            data_writer.writerow(data)

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


contact1 = Contact("George Ti", 134141414, "58 Street", "1st OCt 2002")
print(contact1.__str__())
