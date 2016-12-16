# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

# Open football.csv using 'r' for read
with open('football.csv', 'r') as csvfile:
    myreader = csv.DictReader(csvfile)
    smallest_diff = 100000 # set smallest_dif to large number so that the first instance is definitely smaller
    for row in myreader:   # calc difference for each row between goals and goals allowed
        team_diff = abs(int(row['Goals']) - int(row['Goals Allowed']))
        if team_diff < smallest_diff:
            smallest_diff = team_diff 
            team_with_smallest_diff = row['Team'] 
    print team_with_smallest_diff, "with difference of ", smallest_diff 