#Dependencies
import os
import csv
from pathlib import Path

#File location
csvpath = os.path.join('Resources', 'budget_data.csv')



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #Create empty list

    total_months = []
    total_profits = []
    total_profits_change = []

    #Add values to list
    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(int(row[1]))

    #print('date:', total_month)
    #print('total profits:', total_profit)

    #Calculate the total number of months included in the dataset.
    months = (len(total_months))
    print("Total Months: ", months)

    #Calculate the net total amount of "Profit/Losses"
    profits = (sum(total_profits))
    print("Total: ", profits)

    #Calculate the changes in "Profit/Losses" then find the average of those changes
    i = 0 
    for i in range(len(total_profits) - 1) :
        change = (total_profits[i+1]) - (total_profits[i])

        total_profits_change.append(change)

    total_change = sum(total_profits_change)
    #print(total_change)
    Average_change = total_change / len(total_profits_change)
    print("Average Change: ", Average_change)

    #Find the greatest increase in profits (date and amount) over the entire period
    Max_increase = max(total_profits_change)
    print("Greatest Increase in Profits: ", Max_increase)

    #Find the greatest decrease in profits (date and amount) over the entire period
    Decrease = min(total_profits_change)
    print("Greatest Decrease in Profits: ", Decrease)

#Output File to Text File
output_file = Path('Resources','Financial_Analysis.txt')

with open(output_file,"w") as file: 

    #Write results to be saved to financial analysis txt file
    file.write(f"Election Results")
    file.write(f"---------------------------")
    file.write(f"Total:  {profits}")
    file.write(f"Average Change:  {Average_change}")
    file.write(f"Greatest Increase in Profits:  {Max_increase}")
    file.write(f"Greatest Decrease in Profits: {Decrease}")
    