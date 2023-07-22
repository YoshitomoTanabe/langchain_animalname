## How to use

### 1. Create`.env` file
- Copy `.env.example` file and Input your OpenAI's API Key.
  ```text
    OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  ```

### 2. Prepare and execute

- Check Python version.
  ```bash
    $ python -V
    Python 3.11.3
  ```
- Install module to use `requrements.txt` .
  ```bash
    $ pip install -r requirements.txt
  ```
- Execute on Python.
  ```bash
    $ python __main__.py
  ```
- Enjoy!
  ```bash
    # Execution example
    好きな動物を入力してください。かわいい名前をかんがえるよ。
    動物の種類を入力(「おわり」で終了)：いぬ


    1.くまのこ
    2.シナ
    3.ポチ
    4.サク
    5.ミーコ
  ```