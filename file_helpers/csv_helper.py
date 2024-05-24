import csv

from files import CSV_FILE_PATH


def read_lines_from_csv(limit=10):
    result = []
    with open(CSV_FILE_PATH) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
            if len(result) == limit:
                break
    return result


print(read_lines_from_csv())