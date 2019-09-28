#Import files 
import csv 
import os 

#Path to collect data from the resource folder
Election_data_csv = os.path.join('..' , 'Election_data.csv')

#Define variables  
Total_votescast = 0 
Candidate_List = [] 
Candidate_options = []
Num_ofvotes_cand = 0 
Popular_votewinner = []
candidate_name = []
unique_list = []

#Read the Election_data.csv 
with open(Election_data_csv, newline="") as csvfile:

    #Split the data on commas in Rows
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    # Read through each row to add data to lists 
    for row in csvreader:
       #Voter Id
        ID = row[0]
       #County   
        County = row[1]
       #Candidate 
        Candidate = row[2]
        #print(row[0])
        #print(row[1])
        #print(row[2])

#Total number of votes cast 
        Total_votescast = Total_votescast + 1
        print(Total_votescast)
#complete list of candidates who received votes 
        Candidate_List.append(Candidate)
        #print(Candidate_List)
        unique_list = len(Candidate_List)
        #print(unique_list)

        
#For cand in the set(Candidate_List)
#Candidate_List.append(row[2])
#The percentage of votes each candidate won 
#The total number of votes each candidate won 
#The winner of the election based on popular vote 


