import csv

from utils import db


def uniswap_to_db(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                date = None if row[0]=='NULL' else str(row[0])
                liquidity = None if row[1]=='NULL' else str(row[1])
                value = None if row[2]=='NULL' else str(row[2])
                price = None if row[3]=='NULL' else str(row[3])
                query = ("INSERT INTO uniswap"
                            " (date,liquidity,value,price)"
                            " VALUES (%s, %s, %s, %s)")
                db.sql(query, (date,liquidity,value,price,))

                line_count += 1
        print(f'Processed {line_count} lines.')
