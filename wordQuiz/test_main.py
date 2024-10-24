from itertools import cycle
import unittest
from unittest.mock import patch
from wordQuiz.main import (
    choose_word,
    display_game_state,
    initialize_game_state,
    validate_input,
    update_game_state,
    words
)

class TestHangmanGame(unittest.TestCase):
    """
    単語当てゲームの各関数をテストするためのユニットテストクラス。
    """

    def test_choose_word(self):
        """
        choose_word関数のテスト。
        ランダムに選ばれた単語がリスト内に存在するかを確認します。
        """
        with patch('random.choice', return_value='APPLE'):
            word = choose_word(words)
            self.assertEqual(word, 'apple')
            self.assertIn(word.upper(), [w.upper() for w in words])

    def test_initialize_game_state(self):
        """
        initialize_game_state関数のテスト。
        初期状態が正しく設定されているかを確認します。
        """
        test_word = "test"
        display_word, remaining_attempts, guessed_letters = initialize_game_state(test_word)
        
        self.assertEqual(display_word, ['_', '_', '_', '_'])
        self.assertEqual(remaining_attempts, 5)
        self.assertEqual(guessed_letters, set())

    def test_validate_input_valid_letter(self):
        """
        validate_input関数のテスト。
        有効な入力が正しく検証されるかを確認します。
        """
        guessed_letters = set()
        is_valid, message = validate_input('a', guessed_letters)
        
        self.assertTrue(is_valid)
        self.assertEqual(message, '')

    def test_validate_input_invalid_letter(self):
        """
        validate_input関数のテスト。
        無効な入力が正しく検証されるかを確認します。
        """
        guessed_letters = set('a')
        is_valid, message = validate_input('a', guessed_letters)
        
        self.assertFalse(is_valid)
        self.assertEqual(message, 'その文字は既に入力されています。')

    def test_update_game_state_correct_guess(self):
        """
        update_game_state関数のテスト。
        正解の文字を推測した場合のゲーム状態の更新を確認します。
        """
        hidden_word = "test"
        display_word = ['_', '_', '_', '_']
        remaining_attempts = 5
        guessed_letters = set()
        
        new_display, new_attempts, new_guessed = update_game_state(
            't', hidden_word, display_word, remaining_attempts, guessed_letters
        )
        
        self.assertEqual(new_display, ['t', '_', '_', 't'])
        self.assertEqual(new_attempts, 5)
        self.assertEqual(new_guessed, {'t'})

    def test_update_game_state_incorrect_guess(self):
        """
        update_game_state関数のテスト。
        不正解の文字を推測した場合のゲーム状態の更新を確認します。
        """
        hidden_word = "test"
        display_word = ['_', '_', '_', '_']
        remaining_attempts = 5
        guessed_letters = set()
        
        new_display, new_attempts, new_guessed = update_game_state(
            'x', hidden_word, display_word, remaining_attempts, guessed_letters
        )
        
        self.assertEqual(new_display, ['_', '_', '_', '_'])
        self.assertEqual(new_attempts, 4)
        self.assertEqual(new_guessed, {'x'})

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
                mock_print.assert_any_call(message)
                continue

            display_word, remaining_attempts, guessed_letters = update_game_state(
                guess, hidden_word, display_word, remaining_attempts, guessed_letters
            )

        if "_" not in display_word:
            mock_print.assert_any_call("おめでとうございます！単語を当てました:", hidden_word)
        else:
            mock_print.assert_any_call("ゲームオーバー！正解の単語は:", hidden_word)

if __name__ == '__main__':
    unittest.main()