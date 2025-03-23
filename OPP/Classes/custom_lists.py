import pickle
import os
from content_library import Library

library = Library()
library.load_from_file("dataset.txt")

custom_lists_db = "custom_lists.pkl"

def load_custom_lists():
    if os.path.exists(custom_lists_db) and os.path.getsize(custom_lists_db) > 0:
        with open(custom_lists_db, "rb") as f:
            try:
                return pickle.load(f)
            except (EOFError, pickle.UnpicklingError):
                return {} 
    return {}

def save_custom_lists(data):
    with open(custom_lists_db, "wb") as f:
        pickle.dump(data, f)
    
def create_custom_list(username, list_name):
    data = load_custom_lists()

    if username not in data:
        data[username] = {}

    if list_name in data[username]:
        print(f"A list named '{list_name}' already exists.")
    else:
        data[username][list_name] = []
        save_custom_lists(data)
        print(f"List '{list_name}' created.")

def delete_custom_list(username, list_name):
    data = load_custom_lists()

    if username in data and list_name in data[username]:
        del data[username][list_name]
        save_custom_lists(data)
        print(f"List '{list_name}' has been deleted.")
    else:
        print(f"List '{list_name}' does not exist.")

def add_to_custom_list(username, list_name, content_name):
    data = load_custom_lists()
    
    results = library.search_by_name(content_name)
    if not results:
        print(f"\n '{content_name}' not found in the content library.")
        return
    
    correct_name = results[0].name
    
    if username not in data:
        data[username] = {}

    if list_name not in data[username]:
        data[username][list_name] = []

    if correct_name not in data[username][list_name]:
        data[username][list_name].append(correct_name)
        save_custom_lists(data)
        print(f" '{correct_name}' added to '{list_name}' list.")
    else:
        print(f" '{correct_name}' is already in '{list_name}' list.")

def remove_from_custom_list(username, list_name, content_name):
    data = load_custom_lists()
    if username not in data or list_name not in data[username]:
        print(f"List '{list_name}' does not exist.")
        return

    matching_name = next((c for c in data[username][list_name] if c.lower() == content_name.lower()), None)

    if matching_name:
        data[username][list_name].remove(matching_name)
        save_custom_lists(data)
        print(f"'{matching_name}' removed from '{list_name}'.")
    else:
        print(f"'{content_name}' is not in '{list_name}'.")

def view_custom_lists(username):
    while True:
        data = load_custom_lists()
        print("\n CUSTOM LIST")
        if username in data and data[username]:
            for list_name, content in data[username].items():
                print(f"• {list_name} ({len(content)} items)")
        else:
            print("You have no custom lists.")

        print("\n [1] Create a new list")
        print("\n [2] View a specific custom list")
        print("\n [3] Delete a list")
        print("\n [4] Return")

        choice = input("\n Choose an action: ").strip()

        if choice == "1":
            new_list = input("Enter the name of the new list: ").strip()
            create_custom_list(username, new_list)
        elif choice == "2":
            list_name = input("Enter the name of the list to view: ").strip()
            manage_custom_list(username, list_name)
        elif choice == "3":
            list_name = input("Enter the name of the list to delete: ").strip()
            delete_custom_list(username, list_name)
        elif choice == "4":
            break
        else:
            print("Invalid input.")

def manage_custom_list(username, list_name):
    while True:
        data = load_custom_lists()
        if username not in data or list_name not in data[username]:
            print(f"List '{list_name}' does not exist.")
            return

        print(f"\n {list_name}")
        if data[username][list_name]:
            for idx, content in enumerate(data[username][list_name], 1):
                print(f"{idx}. {content}")
        else:
            print(f"Your '{list_name}' list is empty.")

        print("\n [1] Add content to this list")
        print("\n [2] Remove content from this list")
        print("\n [3] Return")

        sub_choice = input("\n Choose an action: ").strip()

        if sub_choice == "1":
            content_name = input("Enter content name to add: ").strip()
            add_to_custom_list(username, list_name, content_name)
        elif sub_choice == "2":
            content_name = input("Enter content name to remove: ").strip()
            remove_from_custom_list(username, list_name, content_name)
        elif sub_choice == "3":
            break
        else:
            print("Invalid option.")
