#big s/o to my tutor for helping clean this up
#modules
import os
import csv
#set path for the csvfile
csvpath=os.path.join('election_data.csv')

#set variables for later use
total_votes=0
candidates=[]
cand_votes=[]
percent=[]

#open the csvfile
with open(csvpath, newline='') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',')
    #skip the header
    row=next(csvReader,None)
    for row in csvReader:
        #add to total number of votes, adding 1 since each row represents one vote
        total_votes=total_votes+1
        #store candidate value so you can reference it later
        candidate= row[2]
        #creating a list of unique candidate names, and storing vote counts in a new list
        if candidate in candidates:
            candidate_index=candidates.index(candidate)
            cand_votes[candidate_index]=cand_votes[candidate_index]+1
            #if it is a new candidate, create new spot in list for them, and start counting votes
        else:
            candidates.append(candidate)
            cand_votes.append(1)

#https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena
#tallying up percentage of votes and replacing max votes to determine winner
max_votes_cand=cand_votes[0]
max_index=0
for x in range (len(candidates)):
    vote_percentage=round(cand_votes[x]/total_votes*100,2)
    percent.append(vote_percentage)
    if cand_votes[x] > max_votes_cand:
        max_votes_cand=cand_votes[x]
        max_index= x
winner=candidates[max_index]

#print election results
print(f'Election Results')
print(f'-----------------')
print(f'Total Votes: {total_votes}')
for x in range(len(candidates)):
    print(f'{candidates[x]}: {percent[x]}% {cand_votes[x]}')
print(f'------------------')
print(f'Winner: {winner} ')
print(f'-------------------')

#export file to .txt format
filepath=os.path.join('PyPoll.txt')
with open(filepath, 'w', newline='\n') as text:
    text.write(f'Election Results\n')
    text.write(f'--------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    for x in range(len(candidates)):
        text.write(f'{candidates[x]}: {percent[x]}% {cand_votes[x]}\n')
    text.write(f'----------------\n')
    text.write(f'Winner: {winner}')
    
