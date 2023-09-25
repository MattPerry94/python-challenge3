#referencing Module 3- 012- Census Zip

#import
import os
import csv

#Path
csvpath=os.path.join("budget_data.csv")

#Empty List for Later
count_months = []
total_profit = []
montly_change = []

#Open File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#Count the months and get the total profit
    for row in csvreader:
        count_months.append(row[0])
        total_profit.append (int(row[1]))

    for x in range(len(total_profit)-1):
        montly_change.append(total_profit[x+1]-total_profit[x])

maxincrease = max(montly_change)
mindecrease = min(montly_change)

maxmonth = montly_change.index(max(montly_change)) + 1
minmonth = montly_change.index(min(montly_change)) + 1

#Print
print("Financial Analysis")
print(f"Total Months: {len(count_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(montly_change)/len(montly_change))}")
print(f"Greatest Increase in Profits: {count_months[maxmonth]}: ${str(maxincrease)}")
print(f"Greatest Decrease in Profits: {count_months[minmonth]}: ${str(mindecrease)}")


output_file =os.path.join("C:\\Users\\mperry2\\Downloads\\Starter_Code (5)\\Starter_Code\\PyBank\\Resources, Financial Summary.txt")

with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write(f"Total Months: {len(count_months)}")
    file.write(f"Total: ${sum(total_profit)}")
    file.write(f"Average Change: ${round(sum(montly_change)/len(montly_change))}")
    file.write(f"Greatest Increase in Profits: {count_months[maxmonth]}: ${str(maxincrease)}")
    file.write(f"Greatest Decrease in Profits: {count_months[minmonth]}: ${str(mindecrease)}")