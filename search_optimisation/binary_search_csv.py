import csv
import os
import io

def binary_search_csv(filename, target, column_i=0):
    file_size = os.path.getsize(filename)

    with open(filename, "rb") as f:
        #This reads the file as raw binary, which allows us to get the file size
        #and move the cursor around in the file (i.e to move to the middle)
        header = f.readline()
        header_size = f.tell()
        
        low = header_size
        high = file_size

        while low < high:
            mid = (low + high) // 2
            f.seek(mid)

            if mid != 0:
                f.readline()

            current_position = f.tell()

            # If readline() takes us to the end of the file, move the high pointer back
            # If mid == header_size, that means that both low and high have the value of header_size
            if current_position >= high and mid != header_size:
                high = mid
                continue
            
            line = f.readline().decode("utf-8").strip()
            if not line:
                high = mid
                break
            
            reader = csv.reader([line])
            row = next(reader)
            current_val = row[column_i]

            if current_val == target:
                return row
            elif current_val < target:
                low = f.tell()
            else:
                high = mid

