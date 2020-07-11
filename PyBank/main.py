# PyBank Christine Hemphill

import csv

with open("Resources/budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    row = 0
    line_count = 0
    CurrentMonth = ""
    OverallTotal = 0
    GreatestIncreaseMonth = ""
    GreatestIncrease = 0
    GreatestDecreaseMonth = ""
    GreatestDecrease = 0

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            CurrentMonth = (row[0])
            OverallTotal = OverallTotal + int(row[1])
            if int(row[1]) >= 0 and int(row[1]) > GreatestIncrease:
                GreatestIncrease = int(row[1])
                GreatestIncreaseMonth = (row[0])  
            if int(row[1]) < 0 and int(row[1]) < GreatestDecrease:
                GreatestDecrease = int(row[1])
                GreatestDecreaseMonth = (row[0])
            line_count += 1
    
print ("Financial Analysis")
print ('---------------------------')
print (f'Total Months: {line_count - 1}')
print (f'Total: {OverallTotal}')
print (f'Average Change: {int(OverallTotal/(line_count-1))}')
print (f'Greatest Increase in Profits: {GreatestIncreaseMonth} {GreatestIncrease}')
print (f'Greatest Decrease in Profits: {GreatestDecreaseMonth} {GreatestDecrease}')