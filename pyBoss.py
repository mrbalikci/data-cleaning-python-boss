
'''
FROM THIS FORMAT 

Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania


TO THIS FORMAT 

Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA

'''

# Needy files
import os
import csv

# File path to extract and export as csv
file_path =os.path.join('raw_data', 'employee_data1.csv')
file_to_output = "clean_data1.csv"

# Empty list and fixed lists 
ids = []
ids_fixed = []
names = []
first_name_got = []
last_name_got = []
dob = []
dob_fixed = []
ssn = []
ssn_fixed = []
states = []
states_fixed = []

# Opne CSV file
with open(file_path, newline ='') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')

    next(csv_reader, None)
    i = next(csv_reader)
    # print(i) -- NO COLUMN NAME ASSIGNED 

    # Append each clumn into appropirate lists 
    for row in csv_reader:
        ids.append(row[0])
        names.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        states.append(row[4])

# Read ids and fix it and add to empty list 
for id in ids:
    # print(id)
    ids_fixed = ids_fixed + [id]

# Read names and fix it and add to empty list 
for name in names:
    name = name.split()
    # print(name)
    first_name = name[0]
    first_name_got = first_name_got + [first_name]
    # print(first_name)
    last_name = name[1]
    last_name_got = last_name_got + [last_name]
    # print(last_name)

# Read dates and fix it and add to empty list 
for date in dob:
    date = date.replace('-','/')
    dob_fixed = dob_fixed + [date]
    # print(date)

# Read SSNs and fix it (cover first 5 numbers with * ) and add to empty list 
for num in ssn:
    num = list(num)
    num[0:3] = ('*','*', '*')
    num[4:6] = ('*','*')
    joined_ssn = ''.join(num)
    # print(joined_ssn)

    ssn_fixed = ssn_fixed + [joined_ssn]

# Get the states in short form
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Read states and fix it and add to empty list using above information
for state in states:
    # print(state)
    state_abbrev = us_state_abbrev[state]
    # print(state_abbrev)

    states_fixed = states_fixed + [state_abbrev]

# zip all the fixed lists 
clean_data = zip(ids_fixed, first_name_got, last_name_got,
            dob_fixed, ssn_fixed, states_fixed)


# Save it as a csv file 
with open(file_to_output, 'w', newline ='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(clean_data)