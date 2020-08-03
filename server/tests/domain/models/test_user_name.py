import unittest

from app.domain.models import UserName


class TestUserName(unittest.TestCase):
    def test_OK_can_initialize_length_3(self):
        "[正常系]UserNameを作成できる(長さ3)。"
        user_name = UserName("abc")
        self.assertEqual(user_name.value, "abc")

    def test_OK_can_initialize_length_16(self):
        "[正常系]UserNameを作成できる(長さ16)。"
        user_name = UserName("abcdefghijklmnop")
        self.assertEqual(user_name.value, "abcdefghijklmnop")

    def test_NG_throw_error_when_initialize_length_0(self):
        "[異常系]UserNameを作成できない(長さ0)"
        with self.assertRaises(Exception):
            UserName("")

    def test_NG_throw_error_when_initialize_length_2(self):
        "[異常系]UserNameを作成できない(長さ2)"
        with self.assertRaises(Exception):
            UserName("ab")

    def test_NG_throw_error_when_initialize_length_17(self):
        "[異常系]UserNameを作成できない(長さ17)"
        with self.assertRaises(Exception):
            UserName("abcdefghijklmnopq")
