import random
import string

# 単語のリスト
words = ["apple", "banana", "grape", "orange", "mango", "peach", "cherry", "melon", "kiwi", "plum"]

# ランダムに単語を選択
hidden_word = random.choice(words).lower()
display_word = ["_" for _ in hidden_word]
remaining_attempts = 5
guessed_letters = set()

# ゲームの状態を表示する関数
def display_game_state():
    print(" ".join(display_word))
    print(f"残り失敗可能数: {remaining_attempts}")

# ゲームループ
while remaining_attempts > 0 and "_" in display_word:
    display_game_state()
    guess = input("アルファベットを1文字入力してください: ").lower()

    # 入力のバリデーション
    if len(guess) != 1 or guess not in string.ascii_lowercase:
        print("アルファベットの1文字を入力してください。")
        continue

    # 既に入力された文字のチェック
    if guess in guessed_letters:
        print("その文字は既に入力されています。")
        continue

    guessed_letters.add(guess)

    # 入力された文字が単語に含まれているかチェック
    if guess in hidden_word:
        for index, letter in enumerate(hidden_word):
            if letter == guess:
                display_word[index] = guess
    else:
        remaining_attempts -= 1  # ここで残り回数を減少させる

# ゲーム終了時のメッセージ
if "_" not in display_word:
    print("おめでとうございます！単語を当てました:", hidden_word)
else:
    print("ゲームオーバー！正解の単語は:", hidden_word)