import unittest
from unittest.mock import patch, mock_open, MagicMock
import pickle
from watched import add_to_watched, remove_from_watched, view_watched, export_watched_to_file

class TestWatchedListFunctions(unittest.TestCase):

    def setUp(self):
        self.username = "user1"
        self.content_name = "Sample Content"
        self.initial_data = {self.username: []}

    @patch("content_library.Library.search_by_name")
    @patch('watched.save_watched')
    @patch('watched.load_watched', return_value={"user1": []})
    @patch('builtins.input', side_effect=["8.5", "Great content!"])
    def test_add_to_watched(self, mock_input, mock_load, mock_save, mock_search):
        mock_content = MagicMock()
        mock_content.name = "Sample Content"
        mock_search.return_value = [mock_content]
        
        add_to_watched(self.username, self.content_name)
        saved_data = mock_save.call_args[0][0]
        self.assertIn("user1", saved_data)
        self.assertEqual(len(saved_data["user1"]), 1)
        self.assertEqual(saved_data["user1"][0]["name"], "Sample Content")
        self.assertEqual(saved_data["user1"][0]["rating"], 8.5)
        self.assertEqual(saved_data["user1"][0]["comment"], "Great content!")

    @patch('watched.load_watched', return_value={"user1": [{"name": "Sample Content", "rating": 8.5, "comment": "Great!"}]})
    @patch('watched.save_watched')
    @patch('builtins.print')
    def test_remove_from_watched(self, mock_print, mock_save, mock_load):
        remove_from_watched(self.username, "Sample Content")
        saved_data = mock_save.call_args[0][0]
        self.assertEqual(len(saved_data["user1"]), 0)

    @patch('watched.load_watched')
    @patch('builtins.input', side_effect=["3"])
    @patch('builtins.print')
    def test_view_watched(self, mock_print, mock_input, mock_load):
        mock_load.return_value = {
            "user1": [{"name": "Sample Content", "rating": 8.5, "comment": "Great!"}]
        }
        view_watched(self.username)
        mock_print.assert_any_call("\n WATCHED")
        mock_print.assert_any_call("1. Sample Content (Rating: 8.5)")
        mock_print.assert_any_call("Comment: Great!")

    @patch('watched.load_watched')
    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_export_watched_to_file(self, mock_print, mock_open_func, mock_load):
        mock_load.return_value = {
            "user1": [{"name": "Sample Content", "rating": 9.5, "comment": "Amazing!"}]
        }
        filename = "watched_list.txt"
        export_watched_to_file("user1", filename)
        mock_open_func.assert_called_once_with(filename, "w")
        file_handle = mock_open_func.return_value.__enter__.return_value
        file_handle.write.assert_any_call("Title: Sample Content\n")
        file_handle.write.assert_any_call("Rating: 9.5\n")
        file_handle.write.assert_any_call("Comment: Amazing!\n")

if __name__ == "__main__":
    unittest.main()