from ast import NotIn
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
# declare/set total_votes variable to zero
total_votes = 0
# declare empty list of candidate options
candidate_options = []
# declare empty dictionary of candidate votes
candidate_votes =  {} 
# declare variables for Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file. 
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    for row in file_reader:

        # add to the total vote count
        total_votes += 1

        # print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidates
        if candidate_name not in candidate_options: 

            # add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal, setting the entire message equal to a string variable
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count for each candidate in variable "votes"
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes for each candidate and put in "vote percentage"
        vote_percentage = float(votes)/float(total_votes) * 100

        # Determine winning vote count and candidate
        # 1 Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2 If true, then set winning_count = votes and winning percent = vote_percentage
            winning_count = votes
            winning_percent = vote_percentage
            #3 Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

        # Declare candidate results as a f-string literal variable to hold results for each candidate 
        candidate_results = (f'{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n')
        # Print candidate results to the terminal via the variable candidate_results
        print(candidate_results)
        # Save the candidate results to the text file
        txt_file.write(candidate_results)

    # Print the winning candidate summary to the terminal
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
    

# Print the total votes.
#print(total_votes)

# Print the candidate name from each row
#print(candidate_options)

# Print the candidate vote dictionary
#print(candidate_votes)

# Use the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    # txt_file.write("Counties in the Election""\n""---------------------""\n""Arapahoe\nDenver\nJefferson")
