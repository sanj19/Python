# Modules
import os
import csv     # for reading csv files

#results = {}  # Create a dictionary

data = os.path.join("C:\\Users\\sanj1\\OneDrive\\BootCamp\\Week3_Python\\Homework\\election_data.csv")
results = {}
results2 = []
with open(data, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)


    # Read each row of data after the header
    for row in csvreader:
        results[row[0]] = row[2]
        results2.append(row[2])
        
    #print(results)       
#The total number of votes cast
y = len(list(results.values()))
print("Election Results\n-----------------------------------")
print("Total Votes: ", y)

# A complete list of candidates who received votes
    # Using for loop to remove duplicates from list

CandList = list()
DupList = list()
    
for x in results.values() :
    if x not in CandList :
        CandList.append(x)
    else:    
        DupList.append(x)

print(f"List of Candidates are: {CandList}")

#The percentage of votes each candidate won
for i in range(len(CandList)):
    #print(results2.count(CandList[i]))
    print((CandList[i]), ": ", float(results2.count(CandList[i])) / float(y) * 100, "%   (", (results2.count(CandList[i])), ")")
print("----------------------------------")

#The total number of votes each candidate won

#The winner of the election based on popular vote
print("Winner: ", )
print("------------------------------------")
#**********************************************************************************
output_file = os.path.join("C:\\Users\\sanj1\\OneDrive\\BootCamp\\Week3_Python\\Homework\\Python-challenge\\PyPoll\\election_data.txt")

with open(output_file, "w") as text_file:
   text_file.write ("Election Results\n")
   text_file.write ("-------------------------------\n")
   
   text_file.write ("Total Votes: ")
   text_file.write (str(y))
   text_file.write ("\n")
   
for i in range(len(CandList)):
        #print(results2.count(CandList[i]))
    text_file.write (str(CandList[i]))
        #text_file.write ("% ")

    #text_file.write (str(float(results2.count(CandList[i])) / float(y) * 100))
    #text_file.write ("Election Results\n")
    #text_file.write ("%   (")
    #text_file.write ((results2.count(CandList[i])))
    #text_file.write (")")
    #text_file.write ("-------------------------------\n")