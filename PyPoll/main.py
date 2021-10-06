# import dependencies
import csv
import os

# read the csv file
CSV_FILE_PATH = os.path.join("Resources", "election_data.csv")

#output file location for the survey analysis
outputFile = os.path.join("election_Analysis.txt")

#variables 
totalVotes = 0 #variable that holds the total number of votes
candidates = [] #list that holds the candidates
candidateVotes = {} #holds the votes that each candidate receives
winnerCount = 0 # hold the winning count
winningFlavor = ""

# read the csv file
with open(CSV_FILE_PATH) as surveyData:
    #establish csv reader
    csvreader = csv.reader(surveyData)

    #read the header
    header = next(csvreader)
    #move to the first row

    # add on to the total dates
    totalVotes += 1 # same as totalVotes = totalVotes + 1

    # for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1 # same as totalVotes = totalVotes + 1

        #check to see if the voter that was observed are in the list of flavors
        if row[2] not in candidates:
            #add to list if not in list 
            candidates.append(row[2])

            #add the value to dictionary
            candidateVotes[row[2]] = 1

        else:
            #If candidate is already in list add vote
            candidateVotes[row[2]] += 1
#print(candidateVotes)

voteOutput = ""

for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)
    votePercent = (float(votes) / float(totalVotes)) * 100.00
    voteOutput += f"{candidate}: {votePercent:.3f}% ({votes})\n" 
    
    if votes > winnerCount:
        winnerCount = votes
        winningCandidate = candidate
winningCandidateOutput =winningCandidate
   
output = (
    f"\n\nElection Results\n"
    f"-----------------------------\n"
    f"Total Votes: {totalVotes:}\n"
    f"-----------------------------\n"
    f"{voteOutput}"
    f"-----------------------------\n"
    f"Winner: {winningCandidateOutput:}\n"
    f"-----------------------------\n"
   

)

#display output to the terminal
print(output)

#print results to text file
with open(outputFile, "w") as textFile:
    #write output to text file
    textFile.write(output)
