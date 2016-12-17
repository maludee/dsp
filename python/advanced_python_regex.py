# Q1:

import csv
from collections import Counter
import itertools

# Open faculty csv file
input_stream = open('faculty.csv')
reader = csv.reader(input_stream, delimiter = ',')

# Generate list of degrees
reader.next() # skips header row
degrees = [row[1] for row in reader]

# Remove trailing spaces and periods from degree list
neat = [d.strip(' ') for d in degrees]
neat = [n.replace('.', '') for n in neat]

# Separate degrees with spaces
sept = []
for n in neat:
    f = n.split(' ')
    sept.append(f)

# Merge all lists into one list of degrees
merged = list(itertools.chain.from_iterable(sept))

# Count unique instances of degree types
for (k,v) in Counter(merged).iteritems():
    print "%s: %d" % (k, v)
    
    
### Q2:   

import csv
from collections import Counter

# Open faculty csv file
input_stream = open('faculty.csv')
reader = csv.reader(input_stream, delimiter = ',')

# Generate list of titles
reader.next() # skips header row
titles = [row[2] for row in reader]

# Fix typo 'Assistant Professor is Biostatistics
newtitles = [t.replace(' is ', ' of ') for t in titles]

# Count unique titles
for (k,v) in Counter(newtitles).iteritems():
    print "%s: %d" % (k, v)
    
    
### Q3:

import csv

# Open faculty csv file
input_stream = open('faculty.csv')
reader = csv.reader(input_stream, delimiter = ',')

# Print list of email addresses
reader.next() # skips header row
print [row[3] for row in reader]


### Q4

import csv

# Open faculty csv file
input_stream = open('faculty.csv')
reader = csv.reader(input_stream, delimiter = ',')

# Generate list of emails
reader.next() # skips header row
emails = [row[3] for row in reader]

# Generate list of unique email addresses sans name
address = []
for e in emails:
    name, loc = e.split('@')
    if loc not in address:
        address.append(loc)

# Print list of unique email addresses
print address
    
    