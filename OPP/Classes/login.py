import os
import pickle
import actions 

user_db = "users.pkl"
session_file = "session.pkl"

def load_users ():
    if os.path.exists(user_db):
        with open(user_db, "rb") as f:
            return pickle.load(f)
    return {}

def save_users(users):
    with open (user_db, "wb") as f:
        pickle.dump(users,f)

def save_session(username):
    with open(session_file, "wb") as f:
          pickle.dump(username, f)

def load_session():
    if os.path.exists(session_file):
        with open(session_file, "rb") as f:
               return pickle.load(f)
    return None

def clear_session():
     if os.path.exists(session_file):
          os.remove(session_file)

def register():
        while True:
            users = load_users()
            username = input("Enter your username: ").strip()
            if username.lower() == 'back':
                return
            
            if username in users:
                print("Username already exists. Try again or type 'back' to return.")
                continue
            
            password = input("Enter your password: ")
            users[username] = password
            save_users(users)
            print("Registration successful. Welcome to sinimini!")

            save_session(username)
            break

def login():
    while True:
        users = load_users()
        username = input("Username: ")
        if username.lower() == 'back':
            return

        if username not in users:
            print("User does not exist. Try again or type 'back' to return.")
            continue

        password = input("Password: ") 

        if users[username] == password:
            print(f"Welcome back, {username}!")
            save_session(username)
            actions.user_actions(username)
            break
        if password.lower() == 'back':
            return
        else:
            print(f"Password incorrect. Try again or type 'back' to return.")

def logout():
    clear_session()
    print("\n See you later!")
    main()
               
def main():
    while True:
        current_user = load_session()
        
        if current_user:
            print("\n What's new?")
            actions.user_actions(current_user)
        else:
            print("\n No active session found.")
            action = input("Do you want to [1] Register [2] Login: ").strip().lower()
            if action == "1":
                register()
            elif action == "2":
                login()
            else:
                print("Invalid input.")

if __name__ == "__main__":
     main()