import Content


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

''' 
#Example usage
user = User("john_doe", "password123")
user.register("john_doe", "password123")
user.login("john_doe", "password123")

content_status = UserContentStatus(user.username)

action_list = content_status.create_custom_list("Action Movies")

for content in contents[:3]:
    action_list.add_content(content)

content_status.show_custom_lists()

content_status.add_to_watched(contents[0], rating=8)

content_status.add_to_watch_later(contents[1])

content_status.show_content_status()
'''