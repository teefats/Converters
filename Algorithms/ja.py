import re
def mask():
    password = input("Please enter your password")
    substring = password[-4:]
    prestring = password[:-4]
    print(substring)
    print(prestring)    
    jam =re.sub('[0-9]','#',prestring)
    print(jam)
    last = jam + substring
    print(last)
mask()