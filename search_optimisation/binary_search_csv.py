import csv
import os
import io

def binary_search_csv(filename, target):
    file_size = os.path.getsize(filename)

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        low = 0
        high = file_size

        while low < high:
            mid = (low + high) // 2
            f.seek(mid)

            if mid != 0:
                f.readline()

            current_position = f.tell()
            