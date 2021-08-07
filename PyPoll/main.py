#Dependencies
import os
import csv
from typing import Counter

#File location
csvpath = os.path.join('Resources', 'election_data.csv')



with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #Create empty list
    Voter_ID = []
    County = []
    Candidates = []
    Khan = []
    Correy = []
    Li = []
    OTooley = []

    #Add values to list
    for row in csvreader:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidates.append(row[2])


    #Calculate the total number of votes cast.
    votes = (len(Voter_ID))
    print("Total Votes: ", votes)

    #Calculate the total number of votes each candidate received. 
    #print(Candidates)

    for candidate in Candidates:
        if candidate == "Khan":
            Khan.append(Candidates)
            Khan_votes = len(Khan)
        elif candidate == "Correy":
            Correy.append(Candidates)
            Correy_votes = len(Correy)
        elif candidate == "Li":
            Li.append(Candidates)
            Li_votes = len(Li)
        else:
            OTooley.append(Candidates)
            OTooley_votes = len(OTooley)

    #Calculate the percentage of voters each candidate received. 
    Khan_Percentage = (Khan_votes / votes) * 100
    Correy_Percentage = (Correy_votes / votes) * 100
    Li_Percentage = (Li_votes / votes) * 100
    OTooley_Percentage = (OTooley_votes / votes) * 100 

    #Print Results
    print("Khan: ", Khan_Percentage, Khan_votes)
    print("Correy: ", Correy_Percentage, Correy_votes)
    print("Li: ", Li_Percentage, Li_votes)
    print("OTooley: ", OTooley_Percentage, OTooley_votes)

    #Locate the winner based on votes.
    if Khan_votes > max(Correy_votes, Li_votes, OTooley_votes):
        Winner = "Khan"
    elif Correy_votes > max(Khan_votes, Li_votes, OTooley_votes):
        Winner = "Correy"
    elif Li_votes > max(Khan_votes, Correy_votes, OTooley_votes):
        Winner = "Li"
    else:
        Winner = "OTooley"

    print("Winner: ", Winner)

    

