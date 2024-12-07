class UserContentStatus:
   
    def __init__(self, username, film, status, rating=None):
        self.username = username
        self.film = film  
        self.status = status  
        self.rating = rating  

    def __repr__(self):
        return f"UserContentStatus(username='{self.username}', film='{self.film.name}', status='{self.status}', rating={self.rating})"
