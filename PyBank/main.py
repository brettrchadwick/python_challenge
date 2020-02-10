#big s/o to my tutor for helping me with the logic and flow
#modules
import os
import csv

#set path for file
csvpath=os.path.join('budget_data.csv')

#set variables
total_months=0
total_revenue=0
total_revenue_change=0

#open csv file
with open(csvpath, newline="") as csvFile:
    csvReader=csv.reader(csvFile, delimiter=",")
    #store the header
    csv_header=next(csvReader, None)
    #get first rows data
    row=next(csvReader,None)
    total_months=1
    total_revenue=float(row[1])
    revenue=float(row[1])
    prior_revenue=revenue
    revenue_change=0
    total_revenue_change=0
    max_profit_month=row[0]
    max_profit=revenue
    min_profit_month=row[0]
    min_profit=revenue
    #looping through the data in the file
    for row in csvReader:
        #adding to the month counter and getting values for total revenue
        total_months=total_months+1
        total_revenue=total_revenue+float(row[1])

        #calculating change in revenue between current month and prior month, and then adding it to total change
        revenue_change=float(row[1])-prior_revenue
        total_revenue_change= total_revenue_change+revenue_change

        #figuring out if current revenue is a min or max value and then setting variable to it, if conditions apply
        if revenue_change > max_profit:
            max_profit_month=row[0]
            max_profit=revenue_change
        if revenue_change < min_profit:
            min_profit_month=row[0]
            min_profit=revenue_change

        #setting prior revenue to current month revenue before it proceeds to next row of data
        prior_revenue=float(row[1])
#calculating average revenue per month 
average_revenue=total_revenue/total_months

#calculating average revenue change per month
average_revenue_change=total_revenue_change/(total_months-1)

#rounding final values
total_revenue=int(total_revenue)
max_profit=int(max_profit)
min_profit=int(min_profit)
average_revenue_change=round(average_revenue_change,2)
#printing output data
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_revenue_change}")
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit})")

#exporting results to a .txt file (referenced Python Crash Course by Eric Matthes)
filepath=os.path.join('PyBank.txt')
with open(filepath, 'w', newline='\n') as text:
    text.write(f'Financial Analysis\n')
    text.write(f'--------------------\n')
    text.write(f'Total Months: {total_months}\n')
    text.write(f'Total: $ {total_revenue}\n')
    text.write(f'Average Change: ${average_revenue_change}\n')
    text.write(f'Greatest Increase in Profits: {max_profit_month} (${max_profit})\n')
    text.write(f'Greatest Decrease in Profits: {min_profit_month} (${min_profit})')
