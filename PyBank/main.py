import os
import csv
import statistics

budget_csv = os.path.join('..','Resources','budget_data.csv')

with open(budget_csv,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    csvheader = next(csvreader)

    row_count = 0
    net = 0
    monthly_change = 0

# Make a list of difference between each row
    row_diff = []
    previous_row_value = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""

    for row in csvreader:
        # Add each row in file for total count. Use for months since each row is a new month.
        row_count += 1

        # Add up the total for column Profit/Losses.
        net += int(row[1])

        if row_count > 1:
            monthly_change = int(row[1]) - previous_row_value
            row_diff.append(monthly_change)
            
            if monthly_change > 0 and monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_month = row[0]
            elif monthly_change < 0 and monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_month = row[0]

        previous_row_value = int(row[1])

average_change = round(statistics.mean(row_diff),2)

#After loop printing
print("Financial Analysis")
print("-" * 20)
print(f"Total Months: {row_count}")
print(f"Total: ${net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


with open("Results_summary.txt","w+") as summary:
    summary.write("Financial Analysis" + '\n')
    summary.write("-" * 20 + '\n')
    summary.write(f"Total Months: {row_count}" + '\n')
    summary.write(f"Total: ${net}" + '\n')
    summary.write(f"Average Change: ${average_change}" + '\n')
    summary.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})" + '\n')
    summary.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})" + '\n')

summary.close()