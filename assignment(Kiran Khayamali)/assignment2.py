'''Task 3: WAP that first gives 2 options: 
1. Sign up 
2. Sign in 

when 1 is pressed user needs to provide following information 
1. Username, 2. Password, 3. Mobile number 
All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 


Do it using json files, save everything to json and load from json 
'''
#Using JSON as data storage
import json
import os
def register(flag):
    if not os.path.exists('account.json'):
        with open('account.json', 'w') as f:
            json.dump([], f)  
    
    if flag ==1:
        username = input("Enter username :")
        password = input("Enter password :")
        mobile_number = int(input("Enter Mobile number :"))
        user_details={
            "Username" : username,
            "Password" : password,
            "Mobile Number" : mobile_number
        }

        with open('account.json', 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []  
        
        users.append(user_details)
        
        with open('account.json', 'w') as f:
            json.dump(users, f, indent=4)
        print("User registered successfully!")

    elif flag == 2:
        user_username = input("Enter your username : ")
        user_password = input("Enter your password : ")
        credentials_found = False
        with open('account.json', 'r') as f:
            try:
                users = json.load(f)
                for user in users:
                    if (user_username == user["Username"]) and (user_password ==user["Password"]):
                        print(f"Welcome to the device! The mobile number of user {user_username} is {user["Mobile Number"]}")
                        credentials_found = True
                        break
                if not credentials_found:
                    print("Wrong username and/or password!!")
            except json.JSONDecodeError:
                users = [] 

    else:
        print("Choose 1 or 2 to run the program:")

user_input = int(input("Enter 1 to sign up and 2 to sign in :"))
try:
    register(user_input)
except Exception as e:
    print(e)
