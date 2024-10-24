# 単語当てゲーム

このプロジェクトは、Pythonで実装された単語当てゲームです。プレイヤーは隠された単語を推測し、正しい文字を当てることでゲームを進めます。

## ファイルの説明

- `wordQuiz/main.py`: ゲームのメインロジックが含まれています。
- `wordQuiz/test_main.py`: ゲームの各関数をテストするためのユニットテストが含まれています。

## ゲームの実行方法

1. リポジトリをクローンします。
    ```sh
    git clone <リポジトリのURL>
    cd <リポジトリのディレクトリ>
    ```

2. ゲームを実行します。
    ```sh
    python3 wordQuiz/main.py
    ```

## テストの実行方法

1. テストを実行します。
    ```sh
    python3 -m unittest discover -s wordQuiz
    ```

## 関数の説明

### main.py

- `choose_word(words)`: 単語のリストからランダムに単語を選び、小文字に変換して返します。
- `initialize_game_state(hidden_word)`: ゲームの初期状態を設定します。
- `display_game_state(display_word, remaining_attempts)`: 現在のゲームの状態を表示します。
- `validate_input(guess, guessed_letters)`: プレイヤーの入力を検証します。
- `update_game_state(guess, hidden_word, display_word, remaining_attempts, guessed_letters)`: プレイヤーの推測に基づいてゲームの状態を更新します。
- `main()`: 単語当てゲームのメインループを実行します。

### test_main.py

- `TestHangmanGame`: 各関数をテストするためのユニットテストクラス。
    - `test_choose_word()`: `choose_word` 関数のテスト。
    - `test_initialize_game_state()`: `initialize_game_state` 関数のテスト。
    - `test_validate_input_valid_letter()`: `validate_input` 関数の有効な入力のテスト。
    - `test_validate_input_invalid_letter()`: `validate_input` 関数の無効な入力のテスト。
    - `test_update_game_state_correct_guess()`: `update_game_state` 関数の正解の文字を推測した場合のテスト。
    - `test_update_game_state_incorrect_guess()`: `update_game_state` 関数の不正解の文字を推測した場合のテスト。
    - `test_game_loop()`: ゲームのメインループのテスト。

## 実装できなかった点
実行画面では問題ないのですが、無効な入力が正しく検証されるかのユニットテストが正常に実装できませんでした
判定対象が想定していた'その文字は既に入力されています。'ではなく、その次に出力されるメッセージである'残り失敗可能数:n'が判定されていました