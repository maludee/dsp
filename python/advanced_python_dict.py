import csv
from collections import OrderedDict

with open('faculty.csv') as infile:
    reader = csv.reader(infile)

    # Skip header row
    next(reader)
    
    # Make empty dictionary
    faculty_dict = {}
    repeat_name = {}
    firstlastdict = {}
    
    
    for row in reader:
        # Store the last name, first name, and change row 2 so that "of biostatistics" is removed
        lastname = row[0].split()[-1]
        firstname = row[0].split()[0]
        prof = ''.join(row[2].partition('Professor')[0:2])
        
        # Check if last name already exists as key
        if lastname in faculty_dict:
            
            # Update dictionary of repeat last names
            repeat_name[lastname] = repeat_name.get(lastname, 0) + 1
            
            # Remove the key and store the items
            existing = faculty_dict.pop(lastname)
            if repeat_name[lastname] == 1:
    
                # If existing key has only one other person's info
                faculty_dict[lastname] = [existing, row[1:4]]
            
            else:    
                # If more than one person associated with key, append to list
                existing.append(row[1:4])
                faculty_dict[lastname] = existing
        else:
            
            # Add values and keys to dictionary 
            faculty_dict[lastname] = [row[1], prof, row[3]]
            firstlastdict[(firstname, lastname)] = [row[1], prof, row[3]]
            
            # Sort dictionary by last name for Q8
            alphabetized = OrderedDict(sorted(firstlastdict.items(), key = lambda x: x[0][1]))
    
           

    
    # First 3 items for Q6
    print faculty_dict.items()[:3]
    
    # First 3 items for Q7
    print firstlastdict.items()[:3]
    
    # First 3 items for Q8
    print alphabetized.items()[:3]
    