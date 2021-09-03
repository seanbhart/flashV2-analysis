import csv

from utils import db


def stakes_to_db(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                FromAddress = None if row[0]=='NULL' else str(row[0])
                StakeTransactionHash = None if row[1]=='NULL' else str(row[1])
                StakeID = None if row[2]=='NULL' else str(row[2])
                StakeDateTime = None if row[3]=='NULL' else str(row[3])
                AmountIn = None if row[4]=='NULL' else float(row[4])
                MintedAmount = None if row[5]=='NULL' else float(row[5])
                ExpireDateTime = None if row[6]=='NULL' else str(row[6])
                TotalStakedDays = None if row[7]=='NULL' else float(row[7])
                DappRewardAmount = None if row[8]=='NULL' else float(row[8])
                DappPoolAddress = None if row[9]=='NULL' else str(row[9])
                UnstakeTransactionHash = None if row[10]=='NULL' else str(row[10])  
                UnstakeDateTime = None if row[11]=='NULL' else str(row[11])
                UnstakeEarlyBurnedAmount = None if row[12]=='NULL' else float(row[12])
                MatchedAmount = None if row[13]=='NULL' else float(row[13])
                FlashVersion = None if row[14]=='NULL' else int(row[14])
                V2MigrationTransactionHash = None if row[15]=='NULL' else str(row[15])
                query = ("INSERT INTO stakes"
                            " (FromAddress,StakeTransactionHash,StakeID,StakeDateTime,AmountIn,MintedAmount,ExpireDateTime,TotalStakedDays,DappRewardAmount,DappPoolAddress,UnstakeTransactionHash,UnstakeDateTime,UnstakeEarlyBurnedAmount,MatchedAmount,FlashVersion,V2MigrationTransactionHash)"
                            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                db.sql(query, (FromAddress, StakeTransactionHash, StakeID, StakeDateTime, AmountIn, MintedAmount, ExpireDateTime, TotalStakedDays, DappRewardAmount, DappPoolAddress, UnstakeTransactionHash, UnstakeDateTime, UnstakeEarlyBurnedAmount, MatchedAmount, FlashVersion, V2MigrationTransactionHash,))

                line_count += 1
        print(f'Processed {line_count} lines.')
