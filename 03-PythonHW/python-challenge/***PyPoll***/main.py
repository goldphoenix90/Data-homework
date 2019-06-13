import os
import csv

# set file path
csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path, newline="", encoding="UTF8") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    votes = []
    Candidate = []
    Candidate_List= []
    voter_result= []

    for row in csv_reader:
        votes.append(row[0])
        Candidate.append(row[2])

    f= open("Voting Results.txt", "w+")

    Total_votes= len(votes)
    print("Voting Results")
    print("-"*20)
    print(f"Total number of votes: {Total_votes}")
    print("-"*20)

    f.write("Voting Results\n")
    f.write("-"*20 + "\n")
    f.write(f"Total number of votes: {Total_votes}\n")
    f.write("-"*20 + "\n")

    for x in Candidate:
        if x not in Candidate_List:
            Candidate_List.append(x)
    
    for y in range(len(Candidate_List)):
        candidate_votes= Candidate.count(Candidate_List[y])
        percent_votes= round(((candidate_votes/Total_votes)*100),1)
        voter_result.append(percent_votes)
        print(f"{Candidate_List[y]} {percent_votes} % ({candidate_votes})")
        f.write(f"{Candidate_List[y]} {percent_votes} % ({candidate_votes})\n")
    winner_index= voter_result.index(max(voter_result))
    winner= Candidate_List[winner_index]

    print("-"*20)
    print(f"Winner: {winner}")

    f.write("-"*20 + "\n")
    f.write(f"Winner: {winner}")
    f.close()
    # Candidate_1= Candidate_Votes.count(Candidate_List[0])
    # Candidate_2= Candidate_Votes.count(Candidate_List[1])
    # Candidate_3= Candidate_Votes.count(Candidate_List[2])
    # Candidate_4= Candidate_Votes.count(Candidate_List[3])

    # Percent_Vote_1 = round((((Candidate_1) / (Total_votes))*100),2)
    # Percent_Vote_2 = round((((Candidate_2) / (Total_votes))*100),2)
    # Percent_Vote_3 = round((((Candidate_3) / (Total_votes))*100),2)
    # Percent_Vote_4 = round((((Candidate_4) / (Total_votes))*100),2)
   
    # print(f"{Candidate_List[0]} {Percent_Vote_1} % ({Candidate_1})")
    # print(f"{Candidate_List[1]} {Percent_Vote_2} % ({Candidate_2})")
    # print(f"{Candidate_List[2]} {Percent_Vote_3} % ({Candidate_3})")
    # print(f"{Candidate_List[3]} {Percent_Vote_4} % ({Candidate_4})")
    