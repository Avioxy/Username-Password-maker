import time, random

def choice():
    choice_input = input("Would you like a password, username or both?")
    if choice_input.lower() == "password":
        password(15)
    elif choice_input.lower() == "username":
        username()
    elif choice_input.lower() == "both":
        username()
        password(15)
    else:
        print("Beep Boop Baap? I don't think thats an option :/ Please try again!")
        return

def password(strength: int = 8):
    chars = list('abcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_-+={[}]|:;"')    
    pwd = []
    for i in range(strength):
        pwd.append(random.choice(chars))
    print("Generating Password! Beep Boop.. \n\n10% ▌\n")
    time.sleep(1)
    print("37% ▌▌▌\n")
    time.sleep(2)
    print("69% ▌▌▌▌▌▌\n")
    time.sleep(3)
    print("99% ▌▌▌▌▌▌▌▌▌\n")
    time.sleep(4)
    print("Your new fancy shmancy ultra-secure password is:")
    print(''.join(pwd))

def username():
    fav_clr = str(input("What is your favourite colour?\n"))
    fav_hby = str(input("What are you in terms of hobbies? e.g coder\n"))
    fav_nbr = int(input("What is your favourite number?\n"))
    print("Generating Username! Beep Boop.. \n\n10% ▌\n")
    time.sleep(1)
    print("43% ▌▌▌▌\n")
    time.sleep(2)
    print("99% ▌▌▌▌▌▌▌▌▌\n")
    time.sleep(4)
    print(f'Your brand new username is: {fav_clr}{fav_hby}{fav_nbr}')

while True:
    choice()