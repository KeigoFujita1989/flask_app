# 必要なモジュールのインポート
from flask import Flask 

# Flaskをインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあった時の処理
@app.route('/')
def hello():
    return 'hello World!'

# エントリーポイント
if __name__ == '__main__':
    app.run()