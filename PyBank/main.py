import os
import csv

budget_data = []

budget_file = os.path.join("Resources", "budget_data.csv")

with open(budget_file) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
       budget_data.append(row)
    
months = len(budget_data)
total = 0
greatest_inc = ["", 0]
greatest_dec = ["", 0]
profit_losses = []

for entry in budget_data:
    total = total + int(entry[1])


for i in range(1,len(budget_data)):
    entry = budget_data[i]
    prev_entry = budget_data[i-1]
    diff = int(entry[1]) - int(prev_entry[1]) 
    profit_losses.append(diff)
    if (diff > greatest_inc[1]):
        greatest_inc = [entry[0], diff]
    elif (diff < greatest_dec[1]):
        greatest_dec = [entry[0], diff]
    

avg_change = sum(profit_losses) / len(profit_losses)


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})")
print(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")

output_file = os.path.join("Analysis", "output.txt")

with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {months}\n")
    text_file.write(f"Total: ${total}\n")
    text_file.write(f"Average Change: ${avg_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")

