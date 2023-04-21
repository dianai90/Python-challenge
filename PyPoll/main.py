#Dependencies
import os
import csv

#output path
cvspath = os.path.join('PyPoll/Resources/election_data.csv')
output_path = os.path.join('PyPoll/analysis/Election_Results.txt')

#PyPoll Variables
total_votes=0
candidates_all=[]
candidate_votes=[]

#winning candidate
winning_candidate = ""
winning_count = 0

with open(cvspath) as csvfile:
    csvreader = csv.reader(csvfile)

    csvheader=next(csvreader)

    #for each row
    for row in csvreader:
    #Add total vote count
        total_votes+=1
        candidate_list= (row[2])
        if candidate_list in candidates_all:
            candidateindex = candidates_all.index(candidate_list)
            candidate_votes[candidateindex] = candidate_votes[candidateindex] +1
        else:
            candidates_all.append(candidate_list)
            candidate_votes.append(1)

percent = []
max_votes = candidate_votes[0]
max_index = 0

for z in range(len(candidates_all)):
    vote_percentage = round(candidate_votes[z]/total_votes*100,3)
    percent.append(vote_percentage)
    if candidate_votes[z] > max_votes:
        max_votes = candidate_votes[z]
        max_index = z
        electionwinner = candidates_all[max_index]

#Print winning candidate
print ('\n')
print("Election Results")
print("-"*25)
print(f"Total Votes: {total_votes}")
print("-"*25)
for x in range(len(candidates_all)):
    print(f'{candidates_all[x]} : {percent[x]:.3f}% ({candidate_votes[x]})')

#Printing of data analysis results within Terminal
print('Election Results')
print('-'*25)
print(f'Total Votes: {total_votes}')
print('-'*25)
for x in range(len(candidates_all)):
    print(f'{candidates_all[x]} : {percent[x]:.3f}% ({candidate_votes[x]})')
print('-'*25)
print(f'Winner: {electionwinner}')
print('-'*25)
#Printing of data analysis results to text file
with open(output_path, "w+") as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write('-------------------------\n')
    for x in range(len(candidates_all)):
        txtfile.write(f'{candidates_all[x]} : {percent[x]:.3f}% ({candidate_votes[x]})\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {electionwinner}\n')
    txtfile.write('-------------------------\n')
    






