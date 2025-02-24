import login
import os
import pickle    
from content_library import Library 
import watched
import watch_later
import custom_lists

def user_actions(username):
     while True:
          print("\n SINIMINI")
          print("\n [1] View contents")
          print("\n [2] Open 'watched' list")
          print("\n [3] Open 'watch later' list")
          print("\n [4] Open custom lists")
          print("\n [5] Add content")
          print("\n [6] Logout")

          choice = input("\n Choose an action: ").strip()

          if choice == "1":
               view_content()
          elif choice == "2":
                watched.view_watched(username)
          elif choice == "3":
                watch_later.view_watch_later(username)
          elif choice == "4":
                custom_lists.view_custom_lists(username)
          elif choice == "5":
                add_content_interactive()
          elif choice == "6":
                login.logout()
                break
          else:
               print("Invalid input.")

content_db = "content.pkl"
library = Library()
library.load_from_file("dataset.txt")

def load_content_data():
    if os.path.exists(content_db):
        with open(content_db, "rb") as f:
            return pickle.load(f)
    return {}

def save_content_data(data):
    with open(content_db, "wb") as f:
        pickle.dump(data, f)

def view_content():
    if library.contents:
        for content in library.contents:
            print(content)
    else:
        print("\n No content available.")

    print("\n FILMS AND TV SERIES")
    print("\n [1] Find content")
    print("\n [2] Return")
    sub_choice = input("\n Choose an action: ").strip()
    if sub_choice == "1":
        find_content()
    else:
        return
    
def find_content():
    print("\n Search by: ")
    print("\n [1] Name")
    print("\n [2] Genre")
    print("\n [3] Director")
    print("\n [4] Release year")

    choice = input("\n Input: ").strip()

    if choice == "1":
        name = input("\n Enter content name: ").strip()
        results = library.search_by_name(name)
    elif choice == "2":
        genre = input("\n Enter genre: ").strip()
        results = library.search_by_genre(genre)
    elif choice == "3":
        director = input("\n Enter director name: ").strip()
        results = library.search_by_director(director)
    elif choice == "4":
        year = int(input("\n Enter release year: ").strip())
        results = library.search_by_year(year)
    else:
        print("\n Invalid input.")
        return
    
    if results:
        print("\n Results:")
        for movie in results:
            print(movie)
    else:
        print("\n No movies and series found.")   

def add_content_interactive():
    print("\n Enter details about the new content -")
    name = input("\n NAME: ").strip()
    genre_input = input("\n GENRE(S) (comma separated): ").strip()
    director = input("\n DIRECTOR: ").strip()
    
    while True:
        try:
            release_year = int(input("\n RELEASE YEAR: ").strip())
            if release_year < 1888:
                print("Please enter a valid release year (>=1888).")
                continue
            break
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            runtime = int(input("\n RUNTIME (in minutes): ").strip())
            if runtime <= 0:
                print("Runtime should be greater than 0 minutes.")
                continue
            break
        except ValueError:
            print("Invalid input.")

    new_entry = library.add_content(name, genre_input, director, release_year, runtime)
    if new_entry is None:
        return
    else:
        print(f"\n {new_entry.name} has been added to the library.")

def logout():
    from login import logout
    logout()