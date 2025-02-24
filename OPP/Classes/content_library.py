class Content:
    def __init__(self, name, genre, director, release_year, runtime):
        self.name = name
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.runtime = runtime

    def __repr__(self):
        return f"{self.name} ({self.release_year})| {self.director} | {self.genre} | {self.runtime} min"
    
class Library:
    def __init__(self):
        self.contents = []

    def load_from_file(self, file_path):
        with open(file_path, mode="r", encoding="utf-8") as txt_file:
            header = txt_file.readline().strip().split("\t")

            for line in txt_file:
                line_data = line.strip().split("\t")
                
                if len(line_data) < 5:
                    continue

                content = Content(
                    name=line_data[0],
                    genre=line_data[1].split(","),  
                    director=line_data[2],
                    release_year=int(line_data[3]),
                    runtime=int(line_data[4])
                )

                self.contents.append(content)

    def search_by_name(self, name):
        result = [content for content in self.contents if name.lower() in content.name.lower()]
        return result

    def search_by_genre(self, genre):
        result = [content for content in self.contents if genre.lower() in [g.lower() for g in content.genre]]
        return result

    def search_by_director(self, director):
        """Find movies by director."""
        result = [content for content in self.contents if content.director.lower() == director.lower()]
        return result

    def search_by_year(self, year):
        result = [content for content in self.contents if content.release_year == year]
        return result
    
    def content_exists(self, name, release_year):
        for content in self.contents:
            if content.name.lower() == name.lower() and content.release_year == release_year:
                return True
        return False
    
    def add_content(self, name, genre_input, director, release_year, runtime, file_path="dataset.txt"):
        if self.content_exists(name, release_year):
            print(f"\nContent '{name}' ({release_year}) already exists in the library.")
            return None
        genre = [g.strip() for g in genre_input.split(",")]
        
        new_content = Content(name, genre, director, release_year, runtime)
        self.contents.append(new_content)
        
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"\n{name}\t{','.join(genre)}\t{director}\t{release_year}\t{runtime}")
            
        return new_content