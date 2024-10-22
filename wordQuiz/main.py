import random
import string

# 単語のリスト
words = ["apple", "banana", "grape", "orange", "mango", "peach", "cherry", "melon", "kiwi", "plum"]

def choose_word(words):
    return random.choice(words).lower()

def initialize_game_state(hidden_word):
    return ["_" for _ in hidden_word], 5, set()

# ゲームの状態を表示する関数
def display_game_state(display_word, remaining_attempts):
    print(" ".join(display_word))
    print(f"残り失敗可能数: {remaining_attempts}")

def validate_input(guess, guessed_letters):
    if len(guess) != 1 or guess not in string.ascii_lowercase:
        return False, "アルファベットの1文字を入力してください。"
    if guess in guessed_letters:
        return False, "その文字は既に入力されています。"
    return True, ""

def update_game_state(guess, hidden_word, display_word, remaining_attempts, guessed_letters):
    guessed_letters.add(guess)
    if guess in hidden_word:
        for index, letter in enumerate(hidden_word):
            if letter == guess:
                display_word[index] = guess
    else:
        remaining_attempts -= 1
    return display_word, remaining_attempts, guessed_letters

def main():
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