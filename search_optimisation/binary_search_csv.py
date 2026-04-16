import csv
import os
import io

def binary_search_csv(filename, target, column_i=0):
    file_size = os.path.getsize(filename)

    with open(filename, "rb") as f:
        #This reads the file as raw binary, which allows us to get the file size
        #the cursor around in the file (i.e to move to the middle)
        
        low = 0
        high = file_size

        while low < high:
            mid = (low + high) // 2
            f.seek(mid)

            if mid != 0:
                f.readline()

            current_position = f.tell()
            
            line = f.readline().decode("utf-8").strip()
            if not line:
                high = mid
                continue
            
            reader = csv.reader([line])
            row = next(reader)
            current_val = row[column_i]

            if current_val = target:
                return row
            elif current_val < target:
                low = f.tell()
            else:
                high = mid

