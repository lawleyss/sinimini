import unittest
from unittest.mock import patch, mock_open
import pickle

import login  

class TestAuthFunctions(unittest.TestCase):

    def setUp(self):
        self.users = {"user1": "pass1"}
        self.users_pickle = pickle.dumps(self.users)
        self.session_user = "user1"
        self.session_pickle = pickle.dumps(self.session_user)

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=b"")
    def test_load_users_empty(self, mock_file, mock_exists):
        with patch("pickle.load", return_value={}):
            users = login.load_users()
            self.assertEqual(users, {})

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=pickle.dumps({"user1": "pass1"}))
    def test_load_users(self, mock_file, mock_exists):
        users = login.load_users()
        self.assertEqual(users, {"user1": "pass1"})

    @patch("builtins.open", new_callable=mock_open)
    def test_save_users(self, mock_file):
        login.save_users(self.users)
        mock_file.assert_called_with(login.user_db, "wb")
        handle = mock_file()
        handle.write.assert_called()

    @patch("builtins.open", new_callable=mock_open)
    def test_save_session(self, mock_file):
        login.save_session("user1")
        mock_file.assert_called_with(login.session_file, "wb")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=pickle.dumps("user1"))
    def test_load_session(self, mock_file, mock_exists):
        session_user = login.load_session()
        self.assertEqual(session_user, "user1")

    @patch("os.path.exists", return_value=True)
    @patch("os.remove")
    def test_clear_session(self, mock_remove, mock_exists):
        login.clear_session()
        mock_remove.assert_called_with(login.session_file)

    @patch("login.load_users", return_value={})
    @patch("login.save_users")
    @patch("login.save_session")
    def test_register_success(self, mock_save_session, mock_save_users, mock_load_users):
        inputs = ["newuser", "newpass"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as mock_print:
            login.register()
            mock_print.assert_any_call("Registration successful. Welcome to sinimini!")
            mock_save_users.assert_called()
            mock_save_session.assert_called_with("newuser")

    @patch("login.load_users", return_value={"user1": "pass1"})
    def test_register_existing_user_then_back(self, mock_load_users):
        inputs = ["user1", "back"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as mock_print:
            login.register()
            mock_print.assert_any_call("Username already exists. Try again or type 'back' to return.")

    @patch("login.load_users", return_value={"user1": "pass1"})
    @patch("login.save_session")
    @patch("login.actions.user_actions")
    def test_login_success(self, mock_user_actions, mock_save_session, mock_load_users):
        inputs = ["user1", "pass1"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as mock_print:
            login.login()
            mock_print.assert_any_call("Welcome back, user1!")
            mock_save_session.assert_called_with("user1")
            mock_user_actions.assert_called_with("user1")

    @patch("login.load_users", return_value={"user1": "pass1"})
    def test_login_wrong_password_then_back(self, mock_load_users):
        inputs = ["user1", "wrongpass", "back"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as mock_print:
            login.login()
            mock_print.assert_any_call("Password incorrect. Try again or type 'back' to return.")

    @patch("login.load_users", return_value={"user1": "pass1"})
    def test_login_nonexistent_user_then_back(self, mock_load_users):
        inputs = ["nonexistent", "back"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as mock_print:
            login.login()
            mock_print.assert_any_call("User does not exist. Try again or type 'back' to return.")

    @patch("login.load_session", return_value=None)
    def test_main_invalid_action(self, mock_load_session):
        inputs = ["invalid", "q"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as mock_print:
            with self.assertRaises(StopIteration):
                login.main()

if __name__ == "__main__":
    unittest.main()