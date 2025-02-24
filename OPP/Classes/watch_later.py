import pickle
import os
from content_library import Library
import watched

library = Library()
library.load_from_file("dataset.txt")

watch_later_db = "watch_later_content.pkl"

def load_watch_later():
    if os.path.exists(watch_later_db):
        with open(watch_later_db, "rb") as f:
            return pickle.load(f)
    return {}

def save_watch_later(data):
    with open(watch_later_db, "wb") as f:
        pickle.dump(data, f)

def add_to_watch_later(username, content_name):
    data = load_watch_later()
    
    results = library.search_by_name(content_name)
    if not results:
        print(f"\n '{content_name}' not found in the content library.")
        return
    
    correct_name = results[0].name
    
    if username not in data:
        data[username] = []

    if correct_name not in data[username]:
        data[username].append(correct_name)
        save_watch_later(data)
        print(f" '{correct_name}' added to 'watch later' list.")
    else:
        print(f" '{correct_name}' is already in 'watch later' list.")

def remove_from_watch_later(username, content_name):
    data = load_watch_later()

    if username not in data or not data[username]:
        print("Your 'watch later' list is empty.")
        return
    
    matching_name = next((c for c in data[username] if c.lower() == content_name.lower()), None)

    if matching_name:
        data[username].remove(matching_name)
        save_watch_later(data)
        print(f"'{matching_name}' has been removed from your 'watch later' list.")
    else:
        print(f"'{content_name}' is not in your 'watch later' list.")

def move_to_watched(username, content_name):
    data = load_watch_later()

    if username not in data or not data[username]:
        print("Your 'watch later' list is empty.")
        return
    
    matching_name = next((c for c in data[username] if c.lower() == content_name.lower()), None)

    if matching_name:
        data[username].remove(matching_name)
        save_watch_later(data)
        watched.add_to_watched(username, matching_name)
        print(f"'{matching_name}' has been moved to your 'watched' list.")
    else:
        print(f"'{content_name}' is not in your 'watch later' list.")

def view_watch_later(username):
    while True:
        data = load_watch_later()

        print("\n WATCH LATER")
        if username in data and data[username]:
            for idx, content in enumerate(data[username], 1):
                print(f"{idx}. {content}")
        else:
            print("Your 'watch later' list is empty.")
        
        print("\n [1] Add content")
        print("\n [2] Remove content")
        print("\n [3] Move content to 'watched' list")
        print("\n [4] Return")

        choice = input("\n Choose an action: ").strip()

        if choice == "1":
            content_name = input("Enter content name to add: ").strip()
            add_to_watch_later(username, content_name)
        elif choice == "2":
            content_name = input("Enter content name to remove: ").strip()
            remove_from_watch_later(username, content_name)
        elif choice == "3":
            content_name = input("Enter content name to move to 'watched' list: ").strip()
            move_to_watched(username, content_name)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")