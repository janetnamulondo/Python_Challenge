#Import files 
import csv 
import os 

#Path to collect data from the resource folder
Election_data_csv = os.path.join('..' , 'Election_data.csv')

#Define variables  
Total_votescast = 0 
#creating a dictionary for candidate votes that will display Name and number of votes
Candidate_votes = {}
Candidate_options = []
#This will be one name of the winner 
winner = ""
#Total votes for the winner
winning_votes = 0


#Read the Election_data.csv 
with open(Election_data_csv, newline="") as csvfile:

    #Split the data on commas in Rows
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    # Read through each row to add data to lists 
    for row in csvreader:
       #Candidate 
        candidate_name = row[2]

#Total number of votes cast 
        Total_votescast = Total_votescast + 1
#print(Total_votescast)
#Create a forloop for complete list of candidates who received votes 
        if candidate_name not in Candidate_options:
                #Add it to the list of candidates in the running
                Candidate_options.append(candidate_name)
                #print(Candidate_options)
                Candidate_votes[candidate_name]=0
        #With each iteration, we add 1 to the candidate votes.                
        Candidate_votes[candidate_name]=Candidate_votes[candidate_name]+1

#Create a forloop for complete list of 
for key in Candidate_votes.keys():
        if Candidate_votes[key] == max(Candidate_votes.values()):
                winner = key

#The percentage of votes each candidate won 
for i in Candidate_votes:
        percent = round((float(Candidate_votes[i])/Total_votescast)*100,0)

print("Elections Outcome") 
print("--------------------------------------------------------------------------------")
print(f"Total Votes Cast: {Total_votescast} ")
print("------------------------------------------")
for i in Candidate_votes:
    percent = round((float(Candidate_votes[i])/Total_votescast)*100,0)
    print(f" {i} : {percent}% ({Candidate_votes[i]})")
print("------------------------------------------")

print(f"The Winner is {winner}")

