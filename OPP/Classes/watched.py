import pickle
import os
from content_library import Library

library = Library()
library.load_from_file("dataset.txt")

watched_db = "watched_content.pkl"

def load_watched():
    if os.path.exists(watched_db):
        with open(watched_db, "rb") as f:
            return pickle.load(f)
    return {}

def save_watched(data):
    with open(watched_db, "wb") as f:
        pickle.dump(data, f)

def add_to_watched(username, content_name):
    data = load_watched()

    results = library.search_by_name(content_name)
    if not results:
        print(f"\n '{content_name}' not found in the content library.")
        return
    
    correct_name = results[0].name

    if username not in data:
        data[username] = []

    if correct_name not in data[username]:
        while True:
            try:
                rating = float(input(f"Rate '{correct_name}' from 1.0 to 10.0: ").strip())
                if 1.0 <= rating <= 10.0:
                    break
                else:
                    print("Please enter a number between 1.0 and 10.0.")
            except ValueError:
                print("Invalid input.")
        
        comment = input(f"Leave a comment or thoughts about '{correct_name}' (Optional): ").strip()

        data[username].append({
            "name": correct_name,
            "rating": rating,
            "comment": comment
        })
        save_watched(data)
        print(f"'{correct_name}' added to your watched list with a rating of {rating}.")
    else:
        print(f"'{correct_name}' is already in your watched list.")

def remove_from_watched(username, content_name):
    data = load_watched()

    if username not in data or not data[username]:
        print("Your 'watched' list is empty.")
        return
    
    matching_name = next((c for c in data[username] if c['name'].lower() == content_name.lower()), None)

    if matching_name:
        data[username].remove(matching_name)
        save_watched(data)
        print(f"'{matching_name['name']}' has been removed from your 'watched' list.")
    else:
        print(f"'{content_name}' is not in your 'watched' list.")

def export_watched_to_file(username, filename="watched_list.txt"):
    data = load_watched()

    if username not in data or not data[username]:
        print("Your 'watched' list is empty.")
        return

    sorted_content = sorted(data[username], key=lambda x: x['rating'], reverse=True)

    with open(filename, "w") as f:
        f.write(f" {username}'s 'watched' list\n")
        f.write("=" * 50 + "\n")
        for content in sorted_content:
            f.write(f"Title: {content['name']}\n")
            f.write(f"Rating: {content['rating']}\n")
            if content['comment']:
                f.write(f"Comment: {content['comment']}\n")
            f.write("-" * 50 + "\n")
    
    print(f"Your watched list has been exported to '{filename}'.")

def view_watched(username):
    while True:
        data = load_watched()

        print("\n WATCHED")
        if username in data and data[username]:
            for idx, content in enumerate(data[username], 1):
                print(f"{idx}. {content['name']} (Rating: {content['rating']})")
                if content['comment']:
                    print(f"Comment: {content['comment']}")
        else:
            print("Your 'watched' list is empty.")

        print("\n [1] Add content")
        print("\n [2] Remove content")
        print("\n [3] Export to file")
        print("\n [4] Return")

        choice = input("\n Choose an action: ").strip()

        if choice == "1":
            content_name = input("Enter content name to add: ").strip()
            add_to_watched(username, content_name)
        elif choice == "2":
            content_name = input("Enter content name to remove: ").strip()
            remove_from_watched(username, content_name)
        elif choice == "3":
            export_watched_to_file(username)
            break
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
