# test_main.py
import string
import unittest
from unittest.mock import patch
from itertools import cycle
from wordQuiz.main import (
    choose_word, initialize_game_state, display_game_state, validate_input, update_game_state, words
)

class TestWordQuiz(unittest.TestCase):
    """
    ハングマンゲームの各関数をテストするためのユニットテストクラス。
    """

    @patch('builtins.print')
    def test_display_game_state(self, mock_print):
        """
        display_game_state関数のテスト。
        ゲームの状態が正しく表示されるかを確認します。

        Args:
            mock_print (Mock): print関数をモックするためのパッチオブジェクト
        """
        display_word = ["_", "_", "_", "_", "_"]
        remaining_attempts = 5
        display_game_state(display_word, remaining_attempts)
        mock_print.assert_any_call(" ".join(display_word))
        mock_print.assert_any_call(f"残り失敗可能数: {remaining_attempts}")

    def test_validate_input(self):
        """
        validate_input関数のテスト。
        プレイヤーの入力が正しく検証されるかを確認します。
        """
        guessed_letters = set('a')
        self.assertEqual(validate_input('a', guessed_letters), (False, "その文字は既に入力されています。"))
        self.assertEqual(validate_input('1', guessed_letters), (False, "アルファベットの1文字を入力してください。"))
        self.assertEqual(validate_input('b', guessed_letters), (True, ""))

    @patch('builtins.input', side_effect=cycle(['a', 'a', 'b', 'c', 'd', 'e']))
    @patch('builtins.print')
    def test_game_loop(self, mock_print, mock_input):
        """
        ゲームのメインループのテスト。
        ゲームが正しく進行し、終了するかを確認します。

        Args:
            mock_print (Mock): print関数をモックするためのパッチオブジェクト
            mock_input (Mock): input関数をモックするためのパッチオブジェクト
        """
        hidden_word = "mango"
        display_word, remaining_attempts, guessed_letters = initialize_game_state(hidden_word)

        while remaining_attempts > 0 and "_" in display_word:
            display_game_state(display_word, remaining_attempts)
            guess = mock_input().lower()

            is_valid, message = validate_input(guess, guessed_letters)
            if not is_valid:
                mock_print.assert_called_with(message)
                continue

            display_word, remaining_attempts, guessed_letters = update_game_state(
                guess, hidden_word, display_word, remaining_attempts, guessed_letters
            )

        if "_" not in display_word:
            mock_print.assert_called_with("おめでとうございます！単語を当てました:", hidden_word)
        else:
            mock_print.assert_called_with("ゲームオーバー！正解の単語は:", hidden_word)

if __name__ == '__main__':
    unittest.main()