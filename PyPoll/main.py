import os
import csv

votes_file = os.path.join("Resources", "election_data.csv")

votes = []
with open(votes_file) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        found_candidate = False
        candidate = row[2]
        if len(votes) > 0:
            for i in range(0, len(votes)):
                if candidate == votes[i][0]:
                    found_candidate = True
                    votes[i][1] = votes[i][1] + 1
        if (found_candidate == False):
            votes.append([candidate, 1])
        
total = 0
winner = 0
for j in range(len(votes)):
    total = total + votes[j][1]
    if votes[j][1] > votes[winner][1]:
        winner = j

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
for k in range(len(votes)):
    percent = votes[k][1]/total
    print(f"{votes[k][0]}: {percent:.3%} ({votes[k][1]})")
print("-------------------------")
print(f"Winner: {votes[winner][0]}")
print("-------------------------")

output_file = os.path.join("Analysis", "output.txt")

with open(output_file, "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total}\n")
    text_file.write("-------------------------\n")
    for k in range(len(votes)):
        percent = votes[k][1]/total
        text_file.write(f"{votes[k][0]}: {percent:.3%} ({votes[k][1]})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {votes[winner][0]}\n")
    text_file.write("-------------------------\n")