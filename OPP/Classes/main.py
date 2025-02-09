import User


def main():
    print("Welcome to the User Registration and Login System!\n")
    
    
    action = input("Do you want to [1] Register or [2] Login? Enter the number: ")
    
    if action == "1":
        
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        
        new_user = User(username, password)
        new_user.register(username, password)
        
    elif action == "2":
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        existing_user = User(username, password)
        existing_user.login(username, password)
        
    else:
        print("Invalid option. Please enter 1 for Register or 2 for Login.")

if __name__ == "__main__":
    main()
