# Election_Analysis
## Overview of Election Audit
In this election audit, we use a python script to determine and report the total number of votes, the number of votes and percentage of votes for each candidate, and the winner of the election based on the popular vote. In addition, we determine and report the voter turnout of each county, the percentage of total votes for each county, and the county with the highest turnout. These results are printed to the terminal and saved as a text file. 
## Election Audit Results
* A total of 369, 711 votes were cast in this congressional election.
Using a `for` loop to examine each row in the csv file, we counted the total votes using the following code:

    `# Add to the total vote count
    total_votes = total_votes + 1`

* There are three counties in this congressional district: Jefferson, Denver and Arapahoe. Denver County had the highest turnout by far, with 306,055 votes and 82.8% of all the votes. Arapahoe County had the fewest votes, with 24,801 votes and 6.7% of the votes. Jefferson County had a slightly higher turnout, with 38,855 votes and 10.5% of the votes.
Using a `for` loop to examine each row in the csv file, we collected the the names of the counties in a list and tallied their votes using the following code 

You can see a visual breakdown of voter turnout by county below:
* As mentioned above, Denver County had the highest turnout by a very large margin.
* There were three candidates in this congressional elections: Charles Casper Stockholm, Diana Degette, and Ramon Anthony Doane. Charles received 85,213 votes, or 23% of the total votes;Diana Degette received 272,892 votes, or 73.8% of the total votes; and Raymon Anthony Doane received 11,606 votes, or 3.1% of the total votes.
    Within the same `for` loop as used for the counties, we collected thir names into a list and tallied their votes. 
    `# If the candidate does not match any existing candidate add it to
    # the candidate list
    if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

        # And begin tracking that candidate's voter count.
        candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count
    candidate_votes[candidate_name] += 1`
* With a large majority, Diana Degette was the winner of the election. She received 272,892 votes and 73.8% of the vote.
## Election Audit Summary


