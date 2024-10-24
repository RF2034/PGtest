import random
import string

# 単語のリスト
words = ["apple", "banana", "grape", "orange", "mango", "peach", "cherry", "melon", "kiwi", "plum"]

def choose_word(words):
    """
    単語のリストからランダムに単語を選び、小文字に変換して返します。

    Args:
        words (list): 単語のリスト

    Returns:
        str: 選ばれた単語
    """
    return random.choice(words).lower()

def initialize_game_state(hidden_word):
    """
    ゲームの初期状態を設定します。

    Args:
        hidden_word (str): 隠された単語

    Returns:
        tuple: 表示用の単語リスト、残りの試行回数、推測された文字のセット
    """
    return ["_" for _ in hidden_word], 5, set()

def display_game_state(display_word, remaining_attempts):
    """
    現在のゲームの状態を表示します。

    Args:
        display_word (list): 表示用の単語リスト
        remaining_attempts (int): 残りの試行回数
    """
    print(" ".join(display_word))
    print(f"残り失敗可能数: {remaining_attempts}")

def validate_input(guess, guessed_letters):
    """
    プレイヤーの入力を検証します。

    Args:
        guess (str): プレイヤーの推測文字
        guessed_letters (set): 既に推測された文字のセット

    Returns:
        tuple: 入力が有効かどうかのブール値とメッセージ
    """
    if len(guess) != 1 or guess not in string.ascii_lowercase:
        return False, "アルファベットの1文字を入力してください。"
    if guess in guessed_letters:
        return False, "その文字は既に入力されています。"
    return True, ""

def update_game_state(guess, hidden_word, display_word, remaining_attempts, guessed_letters):
    """
    プレイヤーの推測に基づいてゲームの状態を更新します。

    Args:
        guess (str): プレイヤーの推測文字
        hidden_word (str): 隠された単語
        display_word (list): 表示用の単語リスト
        remaining_attempts (int): 残りの試行回数
        guessed_letters (set): 既に推測された文字のセット

    Returns:
        tuple: 更新された表示用の単語リスト、残りの試行回数、推測された文字のセット
    """
    guessed_letters.add(guess)
    if guess in hidden_word:
        for index, letter in enumerate(hidden_word):
            if letter == guess:
                display_word[index] = guess
    else:
        remaining_attempts -= 1
    return display_word, remaining_attempts, guessed_letters

def main():
    """
    単語当てゲームのメインループを実行します。
    """
    hidden_word = choose_word(words)
    display_word, remaining_attempts, guessed_letters = initialize_game_state(hidden_word)

    while remaining_attempts > 0 and "_" in display_word:
        display_game_state(display_word, remaining_attempts)
        guess = input("アルファベットを1文字入力してください: ").lower()

        is_valid, message = validate_input(guess, guessed_letters)
        if not is_valid:
            print(message)
            continue

        display_word, remaining_attempts, guessed_letters = update_game_state(
            guess, hidden_word, display_word, remaining_attempts, guessed_letters
        )

    if "_" not in display_word:
        print("おめでとうございます！単語を当てました:", hidden_word)
    else:
        print("ゲームオーバー！正解の単語は:", hidden_word)

if __name__ == "__main__":
    main()