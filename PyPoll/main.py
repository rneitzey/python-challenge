import os
import csv
import statistics

election_csv = os.path.join('Resources','election_data.csv')

with open(election_csv,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    csvheader = next(csvreader)

    voter_count = 0
    candidate_info = {}

    for row in csvreader:
        # Total votes
        voter_count += 1
        candidate_name = row[2]
        current_votes = candidate_info.get(candidate_name, 0)
        new_votes = current_votes + 1
        candidate_info.update({candidate_name : new_votes})


print("Election results")
print("-" * 20)
print (f"Total Votes: {voter_count}")
print("-" * 20)

for candidate,votes in candidate_info.items():
    print(f"{candidate}: {round((votes/voter_count*100),3)}% ({votes})")
