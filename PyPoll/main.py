import os
import csv

##Initialize some accumulator variables and lists
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
list_of_candidates = ["Khan", "Correy", "Li", "O'Tooley"]
list_of_vote_totals = []

input_file = os.path.join(os.getcwd(), 'Resources', 'election_data.csv')
with open(input_file, newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    next(csv_reader) ##Skip the first row (headers)
    ##Scan through each row and add to appropriate accumulator variable when name encountered
    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] == 'Khan':
            khan_votes = khan_votes + 1
        elif row[2] == 'Correy':
            correy_votes = correy_votes + 1
        elif row[2] == 'Li':
            li_votes = li_votes + 1
        else:
            otooley_votes = otooley_votes + 1
            
    ##store in total votes list for analysis
    list_of_votes = [khan_votes, correy_votes, li_votes, otooley_votes]
    list_of_vote_totals.extend(list_of_votes)
    
    ##Calculate percentages for analysis
    khan_percent = (khan_votes / total_votes)*100
    correy_percent = (correy_votes / total_votes)*100
    li_percent = (li_votes / total_votes)*100
    otooley_percent = (otooley_votes / total_votes) * 100

    ##Find the winner and store as variable
    max_votes = max(list_of_vote_totals)
    max_index = list_of_vote_totals.index(max_votes)
    the_winner = list_of_candidates[max_index]

##Write analysis to text file
output_path = os.path.join(os.getcwd(), 'Analysis', 'results.txt')
with open(output_path, 'w') as text_file:
    text_file.write("Election Results\n--------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n--------------------\n")
    text_file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})\n")
    text_file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})\n")
    text_file.write(f"Li: {li_percent:.3f}% ({li_votes})\n")
    text_file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n")
    text_file.write(f"--------------------\nWinner: {the_winner}\n--------------------")

