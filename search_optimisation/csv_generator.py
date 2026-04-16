import csv
import random as r
from datetime import datetime, timedelta

def generate_transaction_csv(nrows):
    start_date = datetime(2020, 1, 1)
    with open("transaction_data.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["timestamp_str", "transaction_id", "amount"])
        print(f"Generating {nrows} rows...")

        current = start_date
        for i in range(nrows):
            current += timedelta(seconds=r.randint(1, 60))

            transaction_id = 1000000 + i

            amount = round(r.uniform(1.0, 5000.0), 2)

            writer.writerow([current, transaction_id, amount])

            if i % 1000000 == 0 and i > 0:
                print(f"Reached row {i}...")

        return "File generation complete!"
    
print(generate_transaction_csv(50000))


