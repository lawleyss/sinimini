from OPP.Classes import Content


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
        return f"CustomList(name='{self.name}', contents={len(self.contents)} contents)"

