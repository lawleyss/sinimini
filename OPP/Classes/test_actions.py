import unittest
from unittest.mock import patch, MagicMock
from actions import add_content_interactive, user_actions, view_content, Library
import sys
import io

class TestActions(unittest.TestCase):
    
    @patch("builtins.input", return_value="2")
    def test_view_content(self, mock_input):
        mock_library = Library()
        mock_library.contents = ["Movie 1", "Movie 2", "Movie 3"]
        
        with patch('actions.library', mock_library):
            view_content()  

    @patch("builtins.input", side_effect=[
            'Movie Title',
            'Action, Comedy',
            'Director Name',
            '2023',
            '120'
        ])
    @patch.object(Library, 'add_content')
    def test_add_new_content(self, mock_add_content, mock_input):
        mock_library = Library()

        mock_library.contents = []

        mock_new_content = MagicMock()
        mock_new_content.name = 'Movie Title'
        mock_new_content.genre = ['Action', 'Comedy']
        mock_new_content.director = 'Director Name'
        mock_new_content.release_year = 2023
        mock_new_content.runtime = 120

        mock_add_content.return_value = mock_new_content
        mock_library.contents.append(mock_new_content)

        with patch('builtins.print') as mock_print:
            add_content_interactive()
            mock_print.assert_called_with(f"\n {mock_new_content.name} has been added to the library.")

    @patch("builtins.input", side_effect=[
            'Movie Title', 
            'Action, Comedy', 
            'Director Name', 
            '2023',  
            '120' 
        ])
    def test_add_existing_content(self, mock_input):
        mock_library = Library()

        existing_content = MagicMock()
        existing_content.name = 'Movie Title'
        existing_content.genre = ['Action', 'Comedy']
        existing_content.director = 'Director Name'
        existing_content.release_year = 2023
        existing_content.runtime = 120

        mock_library.contents.append(existing_content)

        with patch('builtins.print') as mock_print:
            add_content_interactive() 
            mock_print.assert_called_with(f"\nContent '{existing_content.name}' ({existing_content.release_year}) already exists in the library.")

    @patch('login.logout') 
    @patch('builtins.input', side_effect=['6']) 
    def test_logout(self, mock_input, mock_logout):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        user_actions("test_user")

        mock_logout.assert_called_once()

        self.assertIn("SINIMINI", captured_output.getvalue())

        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    unittest.main()
