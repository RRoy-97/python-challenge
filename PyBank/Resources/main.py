import os
import csv
budget_file = os.path.join('Resources',"budget_data.csv")


#open this CSV
with open ('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        rowcount = len(csvfile.readlines())
        print("Total months:" + str(rowcount))
    total = 0
    for row in csvreader:
        total += int(row[1])
        print("Total months:" + total)




