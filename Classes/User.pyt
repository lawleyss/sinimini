class User:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.watched_movies = []  
        self.watch_later_movies = []  
        self.custom_lists = []  

    def __repr__(self):
        return f"User(username='{self.username}')"








