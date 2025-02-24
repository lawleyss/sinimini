import unittest
from unittest.mock import patch, mock_open
from content_library import Content, Library 

class TestContent(unittest.TestCase):
    def test_repr(self):
        content = Content("Inception", ["Action", "Sci-Fi"], "Christopher Nolan", 2010, 148)
        expected = "Inception (2010)| Christopher Nolan | ['Action', 'Sci-Fi'] | 148 min"
        self.assertEqual(repr(content), expected)

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.dummy_file = (
            "Name\tGenre\tDirector\tReleaseYear\tRuntime\n"
            "Inception\tAction,Sci-Fi\tChristopher Nolan\t2010\t148\n"
            "Titanic\tDrama,Romance\tJames Cameron\t1997\t195\n"
            "Avatar\tAction,Sci-Fi\tJames Cameron\t2009\t162\n"
        )
        self.library = Library()
        self.library.contents = [
            Content("Inception", ["Action", "Sci-Fi"], "Christopher Nolan", 2010, 148),
            Content("Titanic", ["Drama", "Romance"], "James Cameron", 1997, 195),
            Content("Avatar", ["Action", "Sci-Fi"], "James Cameron", 2009, 162)
        ]
    
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_from_file_empty(self, mock_file):
        dummy_empty_file = "Name\tGenre\tDirector\tReleaseYear\tRuntime\n"
        lib = Library()
        with patch("builtins.open", mock_open(read_data=dummy_empty_file)):
            lib.load_from_file("dummy_path.txt")
        self.assertEqual(len(lib.contents), 0)
    
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_load_from_file(self, mock_file):
        lib = Library()
        with patch("builtins.open", mock_open(read_data=self.dummy_file)):
            lib.load_from_file("dummy_path.txt")
        self.assertEqual(len(lib.contents), 3)
        self.assertEqual(lib.contents[0].name, "Inception")
        self.assertEqual(lib.contents[1].director, "James Cameron")
    
    def test_search_by_name(self):
        results = self.library.search_by_name("titan")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Titanic")
    
    def test_search_by_genre(self):
        results = self.library.search_by_genre("sci-fi")
        self.assertEqual(len(results), 2)
        self.assertTrue(any("Inception" in c.name for c in results))
        self.assertTrue(any("Avatar" in c.name for c in results))
    
    def test_search_by_director(self):
        results = self.library.search_by_director("james cameron")
        self.assertEqual(len(results), 2)
        for content in results:
            self.assertEqual(content.director, "James Cameron")
    
    def test_search_by_year(self):
        results = self.library.search_by_year(2010)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Inception")

def test_content_exists(self):
        self.assertTrue(self.library.content_exists("Inception", 2010))
        self.assertTrue(self.library.content_exists("inception", 2010))
        self.assertFalse(self.library.content_exists("Nonexistent", 2020))
    
@patch("builtins.open", new_callable=mock_open)
def test_add_content_new(self, mock_file):
    new_name = "The Matrix"
    new_genre = "Action,Sci-Fi"
    new_director = "The Wachowskis"
    new_year = 1999
    new_runtime = 136
    
    new_content = self.library.add_content(new_name, new_genre, new_director, new_year, new_runtime, file_path="dummy_dataset.txt")
    self.assertIsNotNone(new_content)
    self.assertEqual(new_content.name, new_name)
    self.assertEqual(new_content.director, new_director)
    self.assertEqual(len(self.library.contents), 4)
    
    mock_file.assert_called_with("dummy_dataset.txt", "a", encoding="utf-8")
    expected_write = f"\n{new_name}\t{'Action,Sci-Fi'}\t{new_director}\t{new_year}\t{new_runtime}"
    handle = mock_file()
    handle.write.assert_called_with(expected_write)

@patch("builtins.open", new_callable=mock_open)
def test_add_content_duplicate(self, mock_file):
    duplicate_name = "Inception"
    duplicate_year = 2010
    new_content = self.library.add_content(duplicate_name, "Action,Sci-Fi", "Christopher Nolan", duplicate_year, 148, file_path="dummy_dataset.txt")
    self.assertIsNone(new_content)
    self.assertEqual(len(self.library.contents), 3)

if __name__ == "__main__":
    unittest.main()
