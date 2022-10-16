"""This script takes the state and district ID of a member in the house of representatives
and returns the name and phone number of that representative using dictionaries

Submitted by Reyhan Quayum, rrq2003
"""
filename = True
state = True
district = True
while filename != "" or state != "" or district != "":
    filename = input("What is the name of the file you are interested in?")
    if filename == "":
        break
    open_file = open(filename, encoding="latin1")
    header = open_file.readline()
    processed_header = header.strip("").split(",")
    print(processed_header)  # obtain information for column labels
    open_file.seek(1)
    encompassing_dict = {}
    for line in open_file.readlines():
        processed_line = line.strip("").split(",")
        processed_splitline = [element.strip("") for element in processed_line]
        # Builds each mini dictionary containing information using column labels and the data in the csv
        line_dict = {column: datum for (column, datum) in zip(processed_header,
                                                              processed_splitline)}
        # The key for each mini dictionary value is a tuple with state + district name
        state_district = tuple(i for i in processed_splitline[:2])
        encompassing_dict.update({state_district: line_dict})

    state = input("What is the name of the state you are interested in?")
    if state == "":
        open_file.close()
        break
    state = state.title()
    district = input("What is the district ID you are interested in?")
    if district == "":
        open_file.close()
        break
    district = district.title()

    found_value = encompassing_dict.get((state, district))
    # get method obtains dictionary value using key (key is a tuple)
    if bool(found_value) is True:
        print("The representative for district", district, "in the state of", state, "is",
              found_value.get('Given name'), found_value.get('Family name'), ".",
              "The phone number is", found_value.get('Phone \n'))
    else:
        print("No representative was found for district", district, "in the state of", state)
    open_file.close()
