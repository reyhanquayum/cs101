"""This script reads a csv file of food items and creates a new csv file where the food items are sorted
by energy (kcal)

Submitted by Reyhan Quayum, rrq2003
"""
import csv as csv
import operator as operator

f = open("Food_contents_2019_v2.csv", encoding="latin1")
encompassing_dict = {}
reader = csv.DictReader(f)
for row in reader:
    encompassing_dict[row["Food Name"]] = row
    # convert each energy value to float to be able to properly sort in ascending order
    encompassing_dict[row["Food Name"]]["Energy (kcal)"] = float(encompassing_dict[row["Food Name"]]["Energy (kcal)"])
f.close()
encompassing_dict = dict(sorted(encompassing_dict.items(), key=lambda x:operator.getitem(x[1], "Energy (kcal)"),
                                reverse=True))

f = open("rrq2003_food_contents_by_carbohydrate.csv", "w")
writer = csv.writer(f, delimiter="\t")
for k,v in encompassing_dict.items():
    writer.writerow([k, v])
f.close()