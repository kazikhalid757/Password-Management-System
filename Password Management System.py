import csv

# Initialize the name of the CSV file
csv_file = "D:\Data Science\p_database.csv"

# Check if the CSV file exists or not
try:
    with open(csv_file, 'r') as file:
        pass
except FileNotFoundError:
    # If the file does not exist, create a new file with the header row
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['account_name', 'password'])

# Function to see all the data
def see_alldata():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to insert data into the CSV file
def insert_data():
    # Prompt the user to enter the account name and password
    account_name = input('Enter the name of the account: ')
    password = input('Enter the password: ')

    # Write the account name and password to the CSV file
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account_name, password])

    # Print a message to indicate that the data was inserted successfully
    print("Data inserted successfully!")

# Function to check if the account name exists and retrieve the password
def check_data():
    account_name = input('Enter the name of the account: ')

    # Read the CSV file and search for the account name
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == account_name:
                # If the account name is found, extract the password and print it
                password = row[1]
                print('Password for account', account_name, 'is:', password)
                return

    # If the account name is not found, print an error message
    print('No password found for account:', account_name)


# Prompt the user to select an action
chek= int(input('What you want Insert data press 1 or Check data press 2 or See all data press 3.'))

if(chek==1):
    insert_data()

elif(chek==2):
    check_data()

elif(chek==3):
    see_alldata()

else:
    print('Invalid Input')
