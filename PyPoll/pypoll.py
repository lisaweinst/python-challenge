# Import statements
import os 
import csv


elections_data = os.path.join("..", "Instructions", "election_data.csv")

#having variables for the candidates
total_votes = 0 

l_votes = 0
k_votes = 0
c_votes = 0
o_votes = 0

# open and read the csv file
with open(elections_data,newline="") as elections:
    csvreader = csv.reader(elections,delimiter=",")
    #skip the headers
    header = next(csvreader)
    #go through each row of the csv and then add up the votes from the candidates column
    for row in csvreader:
        total_votes +=1
        #add the khan, correy and o'tooley votes
        if row[2] == "Khan":
            k_votes +=1
        elif row[2] == "O'Tooley":
            o_votes +=1
        elif row[2] == "Li": 
            l_votes +=1
        elif row[2] == "Correy":
            c_votes +=1

 # To find the winner we want to make a dictionary out of the two lists
 #first is the candidates and the second is the votes
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [k_votes, c_votes,l_votes,o_votes]

# zip used to take the list of candiates and their votes
election_candidates_and_votes = dict(zip(candidates,votes))

#obtain the candidate with the most votes
winner = max(election_candidates_and_votes, key=election_candidates_and_votes.get)

# percents of each candidate
k_percent = (k_votes/total_votes) * 100
c_percent = (c_votes/total_votes) * 100
l_percent = (l_votes/total_votes) * 100
o_percent = (o_votes/total_votes) * 100


#outputting results
print(f"Election Results")
print(f"-" * 20)
print(f"Total Votes: {total_votes}")
print(f"-" * 20)
#take the third decimal place of the percents
print(f"Khan: {k_percent:.3f}% ({k_votes})")
print(f"Correy: {c_percent:.3f}% ({c_votes})")
print(f"Li: {l_percent:.3f}% ({l_votes})")
print(f"O'Tooley: {o_percent:.3f}% ({o_votes})")
print(f"-" * 20)
print(f"Winner: {winner}")
print(f"-" * 20)

# Output file with the election results
output_file = "./Election_Results_Summary.txt"
with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary.txt 
    file.write(f"Election Results\n")
    file.write(f"-" * 30)
    file.write("\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"-" * 30)
    file.write("\n")
    file.write(f"Khan: {k_percent:.3f}% ({k_votes})\n")
    file.write(f"Correy: {c_percent:.3f}% ({c_votes})\n")
    file.write(f"Li: {l_percent:.3f}% ({l_votes})\n")
    file.write(f"O'Tooley: {o_percent:.3f}% ({o_votes})\n")
    file.write(f"-" * 30)
    file.write("\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"-" * 30)
