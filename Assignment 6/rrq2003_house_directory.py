"""This script finds the information for representatives from a csv file that the user inputs through its
file name. The user searches for the representative by state and district ID. If a match is found,
the program will return the the Rep's name, phone number and state.

Submitted by Reyhan Quayum, rrq2003
"""

filename = input("What is the name of the file you are interested in?")
open_file = open(filename)
header = open_file.readline()
processed_header = header.strip()  # removes whitespace at the end of the line
split_header = processed_header.split(",")
processed_split_header = [element.lower().strip() for element in split_header]
open_file.tell()
looping = True
while looping is True:
    state = input("What U.S. state are you interested in?")
    if state == "":
        exit()
    low_state = state.lower()
    district = input("What is the district ID?")
    for line in open_file.readlines():
        found_state = False
        found_dist = False
        processed_line = line.strip().split(",")
        processed_splitline = [element.strip() for element in processed_line]
        obtained_district = processed_splitline[2]
        dist = obtained_district.split(" ")
        if dist[-1] == "Large":
            # removes the "At Large" from district name so that the rest is simply the state name
            state_name = "".join(dist[:-2])
        elif dist[-1] == "Delegate" or dist[-1] == "Representative":
            # if the last word is Delegate or Representative, the rest is the state name
            state_name = " ".join(dist[:-1])
        elif any(char.isdigit() for char in dist[-1]):
            # if the last word is the district ID is '2nd' or '3rd', everything else is the state name
            state_name = " ".join(dist[:-1])
        if state_name == state or state_name == low_state:
            found_state = True
        if dist[-1] in district:
            found_dist = True
        if found_state and found_dist:
            name = " ".join(processed_splitline[:2])
            ph = processed_splitline[-1]
            print(f"The representative for district {district} in the state of {state} is {name}. The phone number is"
                  f" {ph}.")
    else:
        print("No match was found")
