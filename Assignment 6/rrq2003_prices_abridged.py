"""This script reads a csv file and makes a 2D list from the data. The user can select which columns to keep from
the csv file and generate a new file containing only those columns

Submitted by Reyhan Quayum, rrq2003
"""
looping = True
while looping is True:
    index = 0
    filename = input("What is the name of the file you are interested in?")
    if filename == "":
        break
    open_file = open(filename)
    header = open_file.readline()
    split_header = header.split("\t")
    split_header[-1] = split_header[-1].strip()  # removes whitespace from last element of split_header
    price_table = [split_header]
    for line in open_file:
        split_line = (line.strip("\n").split())
        price_table.append(split_line)
    print(price_table)

    columns = input("What column numbers would you like to keep? (separate numbers by comma)")
    if columns == "":
        break
    columns = columns.split(",")
    new_columns = []
    for i in columns:
        new_columns.append(int((i.strip(" "))))
    new_price_table = []
    sub_table = []
    for p in price_table:
        for i in p:
            if p.index(i) == 0:
                sub_table.append(i)
            elif p.index(i) in new_columns:
                sub_table.append(i)
            else:
                continue
        new_price_table.append(sub_table)  # sub_table is each sublist of price_table
        sub_table = []
    print(new_price_table)

    open_file.close()
    writing_filename = f"subset {index} of {filename}"
    f = open(writing_filename, "w")
    labels_saved = new_price_table[0]
    f.write("\t".join(labels_saved))

    for row in new_price_table:
        if row == new_price_table[0]:
            continue
        else:
            values_saved = row
            f.write("\t".join(values_saved))
            f.write("\n")
    f.close()
    index += 1
