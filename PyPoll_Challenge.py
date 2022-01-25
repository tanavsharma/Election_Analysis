# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

country_options = []
country_votes = {}

# Track the winning candidate, county, vote & county count, and county percentage.
winning_candidate = ""
winning_country = ""

winning_count = 0
winning_country_count = 0

winning_percentage = 0
winning_country_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    print("--->", headers)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count and county count.
        total_votes += 1
        

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Get the country for each row
        country_name = row[1]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county, add the
        # the county to list.
        if country_name not in country_options:

            country_options.append(country_name)
            country_votes[country_name] = 0
        
        country_votes[country_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    print("County Votes:")
    txt_file.write("County Votes:\n")
    # Retrieve county count and percentage.
    for country_name in country_options:

        # Retrieve county count and percentage.
        county = country_votes[country_name]
        county_percentage = float(county) / float(total_votes) * 100
        county_results = (
            f"{country_name}: {county_percentage:.1f}% ({county:,})\n")  
        
        print(county_results)
        
        txt_file.write(county_results)

        # Determine winning county count, winning percentage, and winning country.
        if (county > winning_country_count) and (county_percentage > winning_country_percentage):
            winning_country_count = county
            winning_country = country_name
            winning_country_percentage = county_percentage

       # Print the winning candidate's results to the terminal.
    winning_county = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_country}\n"
        f"-------------------------\n")
    print(winning_county)

    txt_file.write(winning_county)

    
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)


    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)