def data_admin():
    print("Welcome to the database admin app")
    user_details = {"Tunde":"Splurge8","Titi":"SplurgyD","Gloria": "JamrockY", "admin": "12345"}
    name = input("Please enter your name")
    
    if name in user_details.keys():
        print(user_details)
        password = input("Please enter your password")
        if password == user_details[name]:
            print(f'Hello {name} you are logged on')
            print(user_details[name])
            if name == "admin":
                #show the whole database to the admin account
                print(f'Here is the current user database')
                for key, value in user_details.items():
                    print(f'Name: {key} \t\t Password: {value}')
            else:
                password_change = input("Would you like to change your password? (yes/no)").lower().strip()
                if password_change == "yes":
                    new_password =input("Please what would your new password be?")
                    if len(new_password) >= 8:
                        user_details[name] = new_password
                        print(user_details)
                    else:
                        print(f'Your {new_password} is not the minimum eight characters')
                    print(f'{name} , your password is {user_details[name]}')
                else:
                    print(f'\n Thank you, goodbye')
        else:
            print("Password incorrect")
    else:
        print("Username not in database")



                

    # if len(password) >= 8 and name in user_details.keys():
    #     for value in user_details.values():
    #         if password == value:
    #             print("Logging in...")
    #             print(f'You are logged in {name}')
    #             print(f'What would you like to do today?')
    #             question = (input("Would you like to change your password?")).lower()
    #             if(question == "yes"):
    #                 newpassword = input("Please enter your new password")
    #                 user_details[password] = newpassword
    #                 print(user_details)
    # else:
    #     print("Wrong password")   


data_admin()