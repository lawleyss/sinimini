import unittest
import os
from unittest.mock import patch, MagicMock
from custom_lists import (
    create_custom_list, delete_custom_list, add_to_custom_list, 
    remove_from_custom_list, load_custom_lists, save_custom_lists
)
class FakeContent:
    def __init__(self, name):
        self.name = name

class TestCustomLists(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_custom_lists.pkl"
        global custom_lists_db
        custom_lists_db = self.test_db
        self.mock_library = MagicMock()
        self.mock_library.search_by_name.return_value = [MagicMock(name='Test Content')]

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_create_custom_list(self):
        create_custom_list("user1", "Favorites")
        data = load_custom_lists()
        self.assertIn("user1", data)
        self.assertIn("Favorites", data["user1"])

    def test_delete_custom_list(self):
        create_custom_list("user1", "Favorites")
        delete_custom_list("user1", "Favorites")
        data = load_custom_lists()
        self.assertNotIn("Favorites", data.get("user1", {}))

    def test_add_to_custom_list(self):
        create_custom_list("user1", "Favorites")
        fake_content = FakeContent("Test Content")  
        with patch("custom_lists.library.search_by_name", return_value=[fake_content]):  
            add_to_custom_list("user1", "Favorites", "Test Content")
        data = load_custom_lists()
        self.assertIn("Test Content", data["user1"]["Favorites"])

    def test_remove_from_custom_list(self):
        create_custom_list("user1", "Favorites")
        fake_content = FakeContent("Test Content") 
        with patch("custom_lists.library.search_by_name", return_value=[fake_content]):
            add_to_custom_list("user1", "Favorites", "Test Content")
        remove_from_custom_list("user1", "Favorites", "Test Content")
        data = load_custom_lists()
        self.assertNotIn("Test Content", data["user1"]["Favorites"])

if __name__ == "__main__":
    unittest.main()
