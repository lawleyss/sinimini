class Content:
    def __init__(self, name, genre, director, release_year, runtime):
        self.name = name
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.runtime = runtime

    '''
    def search_by_name(self, name):
        result = [content for content in self.contents if name.lower() in content.name.lower()]
        return result

    def search_by_genre(self, genre):
        result = [content for content in self.contents if genre in content.genre]
        return result

    def search_by_director(self, director):
        result = [content for content in self.contents if content.director == director]
        return result

    def search_by_year(self, year):
        result = [content for content in self.contents if content.release_year == year]
        return result
    '''

    def __repr__(self):
        return f"Content(name='{self.name}', director='{self.director}', genre={self.genre}, year={self.release_year}, runtime={self.runtime})"

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
