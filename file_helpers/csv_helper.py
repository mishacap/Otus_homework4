import csv

from files import CSV_FILE_PATH_CREATE_POSTS, CSV_FILE_PATH_UPDATE_POSTS


def read_lines_from_csv_create(limit=10):
    result = []
    with open(CSV_FILE_PATH_CREATE_POSTS) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
            if len(result) == limit:
                break
    return result

def read_lines_from_csv_update(limit=10):
    result = []
    with open(CSV_FILE_PATH_UPDATE_POSTS) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row)
            if len(result) == limit:
                break
    return result

def read_ids_from_csv_update(limit=10):
    result = []
    with open(CSV_FILE_PATH_UPDATE_POSTS) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result.append(row["id"])
            if len(result) == limit:
                break
    return result
