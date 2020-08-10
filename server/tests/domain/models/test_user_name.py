"""ユーザ名の値オブジェクトのテストクラス.

正常系テストケース.
    * 入力値の長さが3で、オブジェクトを生成できる.
    * 入力値の長さが16で、オブジェクトを生成できる.

異常系テストケース.
    * 入力値の長さが0で、例外が投げられる.
    * 入力値の長さが2で、例外が投げられる.
    * 入力値の長さが17で、例外が投げられる.
"""

import unittest

from app.domain.models import UserName


class TestUserName(unittest.TestCase):
    """UserNameテストクラス."""

    def test_OK_can_initialize_length_3(self):
        """[正常系]入力値の長さが3で、オブジェクトを生成できる."""

        user_name = UserName("abc")
        self.assertEqual(user_name.value, "abc")

    def test_OK_can_initialize_length_16(self):
        """[正常系]入力値の長さが16で、オブジェクトを生成できる."""

        user_name = UserName("abcdefghijklmnop")
        self.assertEqual(user_name.value, "abcdefghijklmnop")

    def test_NG_throw_error_when_initialize_length_0(self):
        """[異常系]入力値の長さが0で、例外が投げられる."""

        with self.assertRaises(Exception):
            UserName("")

    def test_NG_throw_error_when_initialize_length_2(self):
        """[異常系]入力値の長さが2で、例外が投げられる."""

        with self.assertRaises(Exception):
            UserName("ab")

    def test_NG_throw_error_when_initialize_length_17(self):
        """[異常系]入力値の長さが17で、例外が投げられる."""

        with self.assertRaises(Exception):
            UserName("abcdefghijklmnopq")
