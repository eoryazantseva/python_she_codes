import csv

def count_colors(csv_file):
    color_counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
        'yellow': 0
    }

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            color_name = row[2].lower()
            if 'red' in color_name:
                color_counts['red'] += 1
            if 'green' in color_name:
                color_counts['green'] += 1
            if 'blue' in color_name:
                color_counts['blue'] += 1
            if 'yellow' in color_name:
                color_counts['yellow'] += 1

    return color_counts

csv_file = 'colours_20_simple.csv'
color_counts = count_colors(csv_file)

for color, count in color_counts.items():
    print(f"{color}: {count}")

