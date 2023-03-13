import os
import csv

# file path
csvpath = os.path.join('Resources/election_data.csv')

# setting  up lists 
total_votes = list()   
candidate_votes = list() 

total_candidate_vote = {}  
percentage_of_votes = list() 

# reading file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None) 

# reading candidates and counting votes
    for row in csvreader:
        
        voterid, county,rowcandidate = row
        total_votes.append(rowcandidate)
        totalvotes = len(total_votes)
        
        if rowcandidate not in candidate_votes:
            candidate_votes.append(rowcandidate)
            total_candidate_vote[rowcandidate] = 0
        

        total_candidate_vote[rowcandidate] = total_candidate_vote[rowcandidate] + 1
   
    
    # finding out the winner
    winner = max(total_candidate_vote, key= total_candidate_vote.get)

    unique = len(total_candidate_vote)
    unique = int(unique)
    outputvalueslist = list(total_candidate_vote.values())
    outputdirkeylist = list(total_candidate_vote.keys())

    # finding out the percentage of votes for each candidate
    for i in range(0, unique):
        percent = '{:.2%}'.format((outputvalueslist[i] / totalvotes))
        percentage_of_votes.append(percent)
    
    #writing to file
    newfile= open("analysis/PollResults.txt", "w")
    newfile.write("Election Results\n" + "--------------------\n")
    newfile.write(f"Total Votes: {totalvotes}\n")
    newfile.write("--------------------\n")
    for i in range(0, unique):
       newfile. write(f"    {outputdirkeylist[i]}    {percentage_of_votes[i]}   ({outputvalueslist[i]})\n")
    newfile.write("--------------------------\n")
    newfile.write(f"Winner: {winner}\n")
    newfile.write("--------------------------\n")
    newfile.close()
 
    #output to terminal
    print ("    ")
    print("Election Results")
    print("----------------")
    print("    ")
    print(f"Total Votes: {totalvotes}")
    print("--------------------------")
    print( "   ")
    for i in range(0, unique):
        print(f"    {outputdirkeylist[i]}   {percentage_of_votes[i]}   ({outputvalueslist[i]}) ")
    print( "   ")
    print("--------------------------")
    print( "   ")
    print(f"Winner: {winner}")
    print( "   ")
    print("--------------------------")

            