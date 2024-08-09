# import modules to read CSVs
import os
import csv

# create list to store file data
budget_data = []

# create os independant file path
budget_file = os.path.join("Resources", "budget_data.csv")

# open csv file
with open(budget_file) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    # read header row
    header = next(csvreader)
    # read each row into budget_data list
    for row in csvreader:
       budget_data.append(row)
    
# calculate total months by length of list
months = len(budget_data)

# declare varables for calculations
total = 0
greatest_inc = ["", 0]
greatest_dec = ["", 0]
profit_losses = []

# add each value to the total
for entry in budget_data:
    total = total + int(entry[1])

# loop through 2nd to last data and compare with previous data
for i in range(1,len(budget_data)):
    entry = budget_data[i]
    prev_entry = budget_data[i-1]

    # calculate difference with previous entry
    diff = int(entry[1]) - int(prev_entry[1]) 
    # add difference to list
    profit_losses.append(diff)

    #compare with greatest increase and decrease stored data
    if (diff > greatest_inc[1]):
        greatest_inc = [entry[0], diff]
    elif (diff < greatest_dec[1]):
        greatest_dec = [entry[0], diff]
    
# calculate average change
avg_change = sum(profit_losses) / len(profit_losses)

#print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})")
print(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")

# create output file path
output_file = os.path.join("Analysis", "output.txt")

# write output to file
with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {months}\n")
    text_file.write(f"Total: ${total}\n")
    text_file.write(f"Average Change: ${avg_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")

