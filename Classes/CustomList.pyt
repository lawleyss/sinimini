class CustomList:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.films = []  

    def add_film(self, film):
        self.films.append(film)

    def __repr__(self):
        return f"CustomList(name='{self.name}', description='{self.description}', films={len(self.films)} movies)"