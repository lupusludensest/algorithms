import unittest


def login(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("Username and password must be strings")
    if not username.strip() or not password.strip():
        raise ValueError("Username and password are required")
    valid_users = {"admin": "secret123", "user": "pass456"}
    return valid_users.get(username) == password


class TestLogin(unittest.TestCase):

    def test_valid_credentials(self):
        self.assertTrue(login("admin", "secret123"))

    def test_valid_credentials_second_user(self):
        self.assertTrue(login("user", "pass456"))

    def test_wrong_password(self):
        self.assertFalse(login("admin", "wrongpass"))

    def test_wrong_username(self):
        self.assertFalse(login("ghost", "secret123"))

    def test_empty_password_raises(self):
        with self.assertRaises(ValueError):
            login("admin", "")

    def test_empty_username_raises(self):
        with self.assertRaises(ValueError):
            login("", "secret123")

    def test_whitespace_only_password_raises(self):
        with self.assertRaises(ValueError):
            login("admin", "   ")

    def test_none_password_raises(self):
        with self.assertRaises((ValueError, TypeError)):
            login("admin", None)

    def test_integer_password_raises(self):
        with self.assertRaises(TypeError):
            login("admin", 12345)

    def test_password_is_case_sensitive(self):
        self.assertFalse(login("admin", "Secret123"))

    def test_sql_injection_attempt(self):
        self.assertFalse(login("admin' --", "anything"))


if __name__ == "__main__":
    unittest.main(verbosity=2)