# PyPoll Christine Hemphill

import csv

with open("Resources/election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    list_csv = list(csv_reader)

    row = 0
    line_count = 0
    item_count = 0
    TotalVotes = 0
    Candidate_List = {}
    Winner = ""

    for item in list_csv:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            if item[2] not in Candidate_List:
                Candidate_List[item[2]] = 1
                item_count += 1
            else:
                Candidate_List[item[2]] += 1
                item_count = item_count

    line_count += 1

    print ("Election Results")
    print ("----------------")
    print (f"Total Votes: {line_count - 1}")
    print ("----------------")
    zmax = 0
    for x, y in Candidate_List.items():
        z = (y/(line_count-1))*100
        if z > zmax:
            zmax = y
            winner = x
        print (f'{x}: {z:.3f}%, {y}')
    print ("----------------")
    print (f"Winner: {winner}")
    print ("----------------")