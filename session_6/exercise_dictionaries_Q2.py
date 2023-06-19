import csv

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }

colours = []

with open(file="colours_865.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        colours.append(line)
