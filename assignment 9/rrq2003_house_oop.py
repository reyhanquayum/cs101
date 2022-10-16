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

        def __init__(self, state, district, rep):
            self.state_name = state
            self.district_id = district
            self.representative = rep

        # returns the phone number for a Seat by accessing the row of csv file in the form of a dictionary

        def getphone(self, dictionary):
            phone = str(dictionary[phone_label])
            return phone

        # similarly returns the office for a seat by accessing the row of csv file in the form of a dictionary

        def getoffice(self, dictionary):
            office = str(dictionary[office_label])
            return office

        def getfullname(self):
            return str(self.representative)

        # calling a Seat object will return the memory location of the object, this converts it into a readable string

        def __str__(self):
            if self.district_id != "At Large":
                return f"Seat for district {self.district_id} in the state of {self.state_name}. \n" \
                    f"Phone number: {self.phone} \n" \
                    f"Office: {self.office} \n" \
                    f"Representative: {self.representative}"
            else:
                return f"At large seat for the state of {self.state_name}. \n" \
                       f"Phone number: {self.phone} \n" \
                       f"Office: {self.office} \n" \
                       f"Representative: {self.representative}"


    """
    Person is an object that contains the information for a representative's given name, family name, and their
    party affiliation
    """


    class Person:
        party_name = ""

        # constructor for Person where a given name, family name, and party name is set

        def __init__(self, given_name, family_name):
            self.given_name = given_name
            self.family_name = family_name

        # assigns or sets a party

        def assign_party(self, dictionary):
            party_name = str(dictionary[party_label])
            return party_name

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
            if self.party_name != "":
                return f"Representative: {self.getfullname()}, {self.party_name}"
            else:
                return f"Representative: {self.getfullname()}"


    # converts each row of csv file into a dictionary with the header as key and data as value
    reader = csv.DictReader(f)

    for row in reader:
        person = Person("given name", "family name")
        person.given_name = row[given_name_label]
        person.family_name = row[family_name_label]
        person.party_name = person.assign_party(row)

    f.seek(1)
    encompassing_dict = {}

    for row in reader:
        person = Person("given name", "family name")
        person.given_name = row[given_name_label]
        person.family_name = row[family_name_label]
        person.party_name = person.assign_party(row).strip()

        seat = Seat("state", "district", "rep")
        state_district = (row[state_label], row[district_label])
        seat.state_name = row[state_label]
        seat.district_id = row[district_label]
        seat.phone = Seat.getphone(seat, row)
        seat.office = Seat.getoffice(seat, row)
        seat.representative = person.given_name + " " + person.family_name + " (" + person.party_name + ")"
        encompassing_dict.update({state_district: seat})

    asking = True
    while asking is True:
        state_input = input("Enter a state name")
        if state_input == "":
            asking = False
            break
        state_input = state_input.title()
        district_input = input("Enter a district ID")
        if district_input == "":
            asking = False
            break
        district_input = district_input.title()
        input_tuple = (state_input, district_input)
        found_seat = False
        for k in encompassing_dict.keys():
            if input_tuple == k:
                found_seat = encompassing_dict[k]
                print(found_seat)
        if found_seat is False:
            print("State or district ID not found!")
