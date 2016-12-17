import csv

# Open faculty csv file
input_stream = open('faculty.csv')
reader = csv.reader(input_stream, delimiter = ',')

# Create list of email addresses
reader.next() # skips header row
emails = [row[3] for row in reader]

# Write email adresses to emails.csv file
with open ('emails.csv', 'w') as f:
    writer = csv.writer(f)
    for val in emails:
        writer.writerow([val])
        