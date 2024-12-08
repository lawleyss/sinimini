from OPP.Classes import Content


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