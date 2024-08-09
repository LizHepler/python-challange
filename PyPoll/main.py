# import modules to read CSVs
import os
import csv

# create os independant file path
votes_file = os.path.join("Resources", "election_data.csv")

# create list to store votes data
votes = []

# open csv file
with open(votes_file) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    # read header
    header = next(csvreader)

    # read each row
    for row in csvreader:
        # assume candidate not found
        found_candidate = False
        # get the candiate name from the row
        candidate = row[2]
        # if the votes list is not empty, then 
        if len(votes) > 0:
            for i in range(0, len(votes)):
                #check if current candiate is in the votes list
                if candidate == votes[i][0]:
                    #set foudn candiatre to true and add one to the votes for that candidate
                    found_candidate = True
                    votes[i][1] = votes[i][1] + 1
        # if not found, add the canidate to the list with one vote
        if (found_candidate == False):
            votes.append([candidate, 1])
        
total = 0
winner = 0
# loop through votes and find canditate with highest votes and set that index to winner
for j in range(len(votes)):
    total = total + votes[j][1]
    if votes[j][1] > votes[winner][1]:
        winner = j

#print results to console
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

# create output file path
output_file = os.path.join("Analysis", "output.txt")

# write output to file
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