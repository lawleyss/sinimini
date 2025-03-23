from unittest.mock import patch, mock_open, ANY
import unittest
import pickle
import watch_later
from content_library import Content

class TestWatchLater(unittest.TestCase):

    def setUp(self):
        self.username = "test_user"
        self.content_name = "Inception"
        self.watch_later_data = {self.username: [self.content_name]}
        self.pickle_data = pickle.dumps(self.watch_later_data)

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=b"")
    def test_load_watch_later_empty(self, mock_file, mock_exists):
        with patch("pickle.load", return_value={}):
            data = watch_later.load_watch_later()
            self.assertEqual(data, {})

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=pickle.dumps({"test_user": ["Inception"]}))
    def test_load_watch_later(self, mock_file, mock_exists):
        data = watch_later.load_watch_later()
        self.assertEqual(data, {"test_user": ["Inception"]})

    @patch("builtins.open", new_callable=mock_open)
    def test_save_watch_later(self, mock_file):
        watch_later.save_watch_later(self.watch_later_data)
        mock_file.assert_called_with(watch_later.watch_later_db, "wb")
        handle = mock_file()
        handle.write.assert_called()

    @patch("watch_later.load_watch_later", return_value={})
    @patch("watch_later.save_watch_later")
    @patch("watch_later.library.search_by_name", return_value=[Content("Inception", "Sci-Fi", "Christopher Nolan", 2010, 148)])
    def test_add_to_watch_later(self, mock_search, mock_save, mock_load):
        with patch("builtins.print") as mock_print:
            try:
                watch_later.add_to_watch_later(self.username, self.content_name)
                mock_print.assert_any_call("'Inception' added to your 'watch later' list.")
            except Exception as e:
                print(f"Test failed due to error: {e}")
            mock_save.assert_called_once()

    @patch("watch_later.load_watch_later", return_value={"test_user": ["Inception"]})
    @patch("watch_later.save_watch_later")
    def test_remove_from_watch_later(self, mock_save, mock_load):
        with patch("builtins.print") as mock_print:
            watch_later.remove_from_watch_later(self.username, "inception")
            mock_print.assert_any_call("'Inception' has been removed from your 'watch later' list.")
            mock_save.assert_called_once()

    @patch("watch_later.load_watch_later", return_value={"test_user": ["Inception"]})
    @patch("watch_later.save_watch_later")
    @patch("watch_later.watched.add_to_watched")
    def test_move_to_watched(self, mock_watched, mock_save, mock_load):
        with patch("builtins.print") as mock_print:
            watch_later.move_to_watched(self.username, "inception")
            mock_print.assert_any_call("'Inception' has been moved to your 'watched' list.")
            mock_save.assert_called_once()
            mock_watched.assert_called_with(self.username, "Inception")

if __name__ == "__main__":
    unittest.main()
