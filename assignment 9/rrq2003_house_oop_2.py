"""Creates a directory of representatives using OOP, a Person class is defined to get the information on each
state-district representative

Submitted by Reyhan Quayum, rrq2003
The same problem handled before but using object oriented programming.
In particular, constructors, get-methods and set-methods are used.
Two classes are defined: Seat, which contains the information for the seat
and Person, which contains the information for the representative.
"""


import csv

filename = input("What is the name of the file you are interested in?")
try:
    f = open(filename)
except FileNotFoundError:
    print("Filename " + filename + " was not found")
else:

    state_label = "State or Territory"
    district_label = "District or Representation Type"
    phone_label = "Phone "
    office_label = "Office Room "
    given_name_label = "Given name"
    family_name_label = "Family name"
    party_label = "Party "

    """
    Class Seat is an object type that has two parameters, state and district ID
    the object contains the phone number and the office for that particular seat
    and also has a method to convert the object into a string to easily see the information for a given seat
    """

    class Seat:
        phone = ""
        office = ""

        # constructor for Seat, each Seat must have a state and district

        def __init__(self, state, district):
            self.state_name = state
            self.district_id = district

        # returns the phone number for a Seat by accessing the row of csv file in the form of a dictionary

        def getphone(self, dictionary):
            phone = str(dictionary[phone_label])
            return phone

        # similarly returns the office for a seat by accessing the row of csv file in the form of a dictionary

        def getoffice(self, dictionary):
            office = str(dictionary[office_label])
            return office

        # calling a Seat object will return the memory location of the object, this converts it into a readable string

        def __str__(self):
            return f"Seat for district {self.district_id} in the state of {self.state_name}. \n" \
                   f"Phone number: {self.phone} \n" \
                   f"Office: {self.office}"
    """
    Person is an object that contains the information for a representative's given name, family name, and their
    party affiliation
    """

    class Person:
        # constructor for Person where a given name, family name, and party name is set
        def __init__(self, given_name, family_name, party_name):
            self.given_name = given_name
            self.family_name = family_name
            self.party_name = party_name

        # retrieves given name of a representative as a string

        def getgivenname(self):
            return str(self.given_name)

        # retrieves family name of a representative as a string

        def getfamilyname(self):
            return str(self.family_name)

        # retrieves full name (given + family name) of a representative as a string

        def getfullname(self):
            return f"{self.given_name} {self.family_name}"

        # string method to return Person object as a readable string with full name and party affiliation

        def __str__(self):
            return f"Representative: {self.getfullname()}, {self.party_name}"

    # converts each row of csv file into a dictionary with the header as key and data as value
    reader = csv.DictReader(f)

    for row in reader:
        person = Person("given name", "family name", "party name")
        person.given_name = row[given_name_label]
        person.family_name = row[family_name_label]
        person.party_name = row[party_label]
        print(str(person))
