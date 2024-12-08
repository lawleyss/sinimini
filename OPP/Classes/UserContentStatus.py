from OPP.Classes import CustomList


class UserContentStatus:
    def __init__(self, username):
        self.username = username
        self.watched = []  
        self.watch_later = []  
        self.custom_lists = []

    def add_to_watched(self, content, rating=None):
        if content not in self.watched:
            if rating is None:
                rating = float(input(f"Please rate '{content.name}' (0-10): "))  # Prompt user for rating
            self.watched.append((content, rating))
            print(f"Added '{content.name}' to watched list with rating: {rating}")
        else:
            print(f"'{content.name}' is already in watched list.")

    def add_to_watch_later(self, content):
        if content not in self.watch_later:
            self.watch_later.append(content)
            print(f"Added '{content.name}' to watch later list.")
        else:
            print(f"'{content.name}' is already in watch later list.")

    def create_custom_list(self, list_name):
        custom_list = CustomList(list_name)
        self.custom_lists.append(custom_list)
        print(f"Custom list '{list_name}' created.")
        return custom_list

    def show_content_status(self):
        print("\nWatched Content:")
        for content, rating in self.watched:
            print(f"- {content.name} (Rating: {rating})")
        
        print("\nWatch Later Content:")
        for content in self.watch_later:
            print(f"- {content.name}")

    def show_custom_lists(self):
        if self.custom_lists:
            print("\nCustom Lists:")
            for custom_list in self.custom_lists:
                print(f"- {custom_list.name}: {len(custom_list.contents)} contents")
        else:
            print("No custom lists created yet.")