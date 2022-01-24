# 必要なモジュールの取り込み
from flask import Flask

# Flaskオブジェクトの生成 --- (*1)
app = Flask(__name__)

# ルート( / )へアクセスがあった時の処理を記述 --- (*2)
@app.route("/")
def index():
  return 'asafafa'

# サーバーを起動 --- (*3)
if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=8080)