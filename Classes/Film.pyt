class Film:
   
    def __init__(self, name, runtime, director, genre, release_year):
        self.name = name
        self.runtime = runtime  
        self.director = director
        self.genre = genre
        self.release_year = release_year

    def __repr__(self):
        return f"Film(name='{self.name}', director='{self.director}', genre='{self.genre}', year={self.release_year})"