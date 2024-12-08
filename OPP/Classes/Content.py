class Content:
    def __init__(self, name, genre, director, release_year, runtime):
        self.name = name
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.runtime = runtime

    def __repr__(self):
        return f"Content(name='{self.name}', director='{self.director}', genre={self.genre}, year={self.release_year}, runtime={self.runtime})"
