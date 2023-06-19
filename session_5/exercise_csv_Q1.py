import csv
with open(file="colours_20_simple.csv", mode="r", encoding="utf-8") as colors_file:
    csv_reader = csv.reader(colors_file, delimiter=" ")
    for row in csv_reader:
        print(row)