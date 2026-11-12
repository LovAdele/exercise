from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # 监听 0.0.0.0 使局域网内其他设备可通过 http://<本机IP>:8000 访问
    app.run(host="0.0.0.0", port=8000, debug=True)
