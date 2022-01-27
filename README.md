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

#
### Election-Audit Results:
- How many votes were cast in this congressional election?
<img src="/Resources/total_votes.png" alt="total_votes" width="250">

#### Here is a breakdown of what we did to achieve this:

1. let start of by importing important modules, which wiill make it easier for us to analyze our data
   ```
   import csv
   import os
   ```
   
   Here are two links that will help you understand the importance of `csv` and the `os` module. <br>
   csv - https://docs.python.org/3/library/csv.html<br>
   os  - https://docs.python.org/3/library/os.html

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
#   
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

<img src="/Resources/county_votes.png" alt="county_votes" width="250"><br>
#### Here is a breakdown of what we did to achieve this:<br>

1. First thing we have to do, is create two variables; one will be an array, which will hold all the unique countries in the data file, and one will be a dictionary which will hold the country name and the total vote count of that country.
   
   ```
   country_options = [] # will hold the unique countries
   country_votes = {} # dictionary of the country name and vote count
   ```


2. To load the country column we need to know which index it lies in. To do this, we can use the next function to print the first line of the file, which will be   the column names. 
   ```
   headers = next(file_reader)
   print(headers)
   ```
   Output:
   
   <img src="/Resources/headers.png" alt="headers" width="450"><br>
   
   An array stores values in indexes, and an index always starts at 0. In this case:<br> `Ballot ID = Index 0`<br> `County = Index 1`<br> `Candidate = Index 2`<br>
   
3. Once we know the index of the column we need to use; in this case it would `County` which is `Index 1`. We can store all the rows in that column to a variable. 
   ```
   country_name = row[1]
   ```

4. Next we need to run an if condition, which checks to see if there are any countys in the csv file, that isnt in our `country_options` array. If the condition is true, we want to add the country names in the data file to the `country_options` array. Next we need to initialize the starting count to zero for each county. Once the name is added, we will increse the counter for that county by 1. This process will continue untill it reaches the end of the csv file. 
   ```
   if country_name not in country_options: # if the name of the county in the csv file isn't in the county_options array, then go to next line.

            country_options.append(country_name) # if condition true, then take that county name and added it to country_name array.
            country_votes[country_name] = 0 # save country_name along with its votes to country dictionary
        
        country_votes[country_name] += 1 # increment the counter, whenever the name occurs. 
   ```
   
5. Next we can get the percentage of the county votes, by running a for loop, that will cycle through the countries in our array and convert the number of votes to percentage by dividing it from the total count. 
   ```
   for country_name in country_options: # for each country in array, do the following:
   
        county = country_votes[country_name] # We will save the country name and vote count, into variable county
        county_percentage = float(county) / float(total_votes) * 100 # converting the vote count to percentage 
        county_results = (
            f"{country_name}: {county_percentage:.1f}% ({county:,})\n")  
        
        print(county_results) ## printing the result
   ```
#
- Which county had the largest number of votes?
  The county with the largest number of votes is Denver. As shown below:
  <img src="/Resources/county_votes.png" alt="county_votes" width="250"><br>
  We can see that Denver had the largest percentage at 82.8% and 305,055 votes. 
#
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  <img src="/Resources/candidate_votes.png" alt="candidate_votes.png" width="450"><br>
  #### Here is a breakdown of what we did to achieve this:<br>
  
  1. First thing we have to do, is create two variables; one will be an array, which will hold all the unique names of the candidates from the data file, and one will be a dictionary which will hold the candidate name and the total vote count for that candidate.
        
   ```
   candidate_options = [] # will hold the unique countries
   candidate_votes = {} # dictionary of the country name and vote count
   ```
  2. Since we already know the column names and their indexes from our previous steps, we can access the all the rows and save them into a variable. 
     ```
     candidate_name = row[2]
     ```
  4. Next we need to run an if condition, which checks to see if there are any candidates in the csv file, that isnt in our `candidate_options` array. If the condition is true, we want to add the candidate name from the data file to the `candidate_options` array. Next we need to initialize the starting count to zero for each candidate. Once the name is added, we will increse the counter for that candidate by 1. This process will continue untill it reaches the end of the csv file.
     ```
     if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
     ```
  6. Next we can get the percentage of the candidate votes, by running a for loop, that will cycle through the candidates in our array and convert the number of votes to percentage by dividing it from the total count. 
     ```
         for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
     ```
#
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
From our analysis above, we can see that election was won by **Diana DeGette** with **272,892**. That is **73.8%** from the total votes casted.
