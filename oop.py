class Content:
    def __init__(self, name, genre, director, release_year, runtime):
        self.name = name
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.runtime = runtime

    def __repr__(self):
        return f"Content(name='{self.name}', director='{self.director}', genre={self.genre}, year={self.release_year}, runtime={self.runtime})"

class CustomList:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_content(self, content):
        if isinstance(content, Content):  
            self.contents.append(content)
            print(f"Added '{content.name}' to the list '{self.name}'.")
        else:
            print("Invalid content. Must be an instance of Content.")

    def remove_content(self, content):
        if isinstance(content, Content) and content in self.contents:
            self.contents.remove(content)
            print(f"Removed '{content.name}' from the list '{self.name}'.")
        else:
            print("Content not found in list or invalid content.")

    def search_by_name(self, name):
        """Search for content by name"""
        result = [content for content in self.contents if name.lower() in content.name.lower()]
        return result

    def search_by_genre(self, genre):
        """Search for content by genre"""
        result = [content for content in self.contents if genre in content.genre]
        return result

    def search_by_director(self, director):
        """Search for content by director"""
        result = [content for content in self.contents if content.director == director]
        return result

    def search_by_year(self, year):
        """Search for content by release year"""
        result = [content for content in self.contents if content.release_year == year]
        return result

    def __repr__(self):
        return f"CustomList(name='{self.name}', contents={len(self.contents)} contents)"

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

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self, username, password):
        self.username = username
        self.password = password
        print(f"Account for {username} created.")

    def login(self, username, password):
        if self.username == username and self.password == password:
            print(f"Welcome back, {username}!")
        else:
            print("Invalid username or password.")

contents = []

with open('dataset.txt', mode='r', encoding='utf-8') as txt_file:
    header = txt_file.readline().strip().split('\t')

    for line in txt_file:
        line_data = line.strip().split('\t')

        content = Content(
            name=line_data[0],
            genre=line_data[1].split(','),  
            director=line_data[2],
            release_year=int(line_data[3]),
            runtime=int(line_data[4])
        )

        contents.append(content)

# Example usage
# Create a user and register
user = User("john_doe", "password123")
user.register("john_doe", "password123")
user.login("john_doe", "password123")

# Create UserContentStatus object for the user
content_status = UserContentStatus(user.username)

# Create a custom list and add some content to it
action_list = content_status.create_custom_list("Action Movies")

# Add some content to the custom list (for example, add the first 3 contents)
for content in contents[:3]:
    action_list.add_content(content)

# Show custom lists and their contents
content_status.show_custom_lists()

# Add content to watched list with rating
content_status.add_to_watched(contents[0], rating=8)

# Add content to watch later list
content_status.add_to_watch_later(contents[1])

# Show the user's watched content and watch later content
content_status.show_content_status()
