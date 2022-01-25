# Election_Analysis

### Overview of Election Audit 

We need to use the information provided in our **election_results.csv** file to find:
- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout


### Election-Audit Results:

### - How many votes were cast in this congressional election?
<img src="/Resources/total_votes.png" alt="total_votes" width="250">

#### Here is a breakdown of what we did to achieve this:

1. let start of by importing important dependencies, which wiill make it easier for us to analyze our data
   ```
   import csv
   import os
   ```

2. lets create a variable and load our data file into it <br>
   ```
   file_to_load = os.path.join("Resources", "election_results.csv")
   ```
   
3. lets create a variable called total_votes, which hold the total votes casted through out the election: <br>
   ```
   total_votes = 0
   ```
   
4. lets open the file as a variable, so we can access it easier<br>
   ```
   with open(file_to_load) as election_data:
   ```
   
   now i can use the variable `election_data` to access the open file known as `election_results.csv`
   
5. once the file is open, we need to read the file so python can understand it. This can be done with python built in reader function<br>
   ```
   file_reader = csv.reader(election_data)
   ```
   
6. once the file has been read and is now able to be understood by python, we can cycle through each row, and increment the `total_votes` variable by 1 for each row in our csv file <br>
   ```
   for row in file_reader:
   
        # Add to the total vote count and county count.
        total_votes += 1
   ```
7. here is what your final code should look like for getting the total vote counts:
   ```
   import csv
   import os
   
   file_to_load = os.path.join("Resources", "election_results.csv")
   
   total_votes = 0
   
   with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        
        for row in file_reader:
            total_votes += 1

   ```
   

  
  
  
### - Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
### - Which county had the largest number of votes?
### - Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
### - Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
