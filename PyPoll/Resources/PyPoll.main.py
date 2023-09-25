#referencing Module 3- 012- Census Zip

#import
import os
import csv

#Path
csvpath=os.path.join("election_data.csv")

#Need to set vote counter to 0
count_votes = 0
DeGette_votes = 0
Stockham_votes = 0
Doane_votes = 0

#Open File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        
        #Count the vote
        count_votes += 1

    if row[2] == "Diana DeGette":
        DeGette_votes += 1


#Print
print("Election Results")
print(f"Total Votes: {count_votes}")
print(f"DeGette Votes: {DeGette_votes}")
print(f"Stockham Votes: {Stockham_votes}")
print(f"Doane Votes: {Doane_votes}")
