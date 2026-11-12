"""Hands-on 1 - a minimal Flask app served on port 8000 to the local network."""

import socket

from flask import Flask, render_template

app = Flask(__name__)

HOST = "0.0.0.0"  # listen on every interface so other machines can reach it
PORT = 8000


def get_lan_ip() -> str:
    """Return this machine's LAN IP (best effort, no traffic is sent)."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        sock.close()


@app.route("/")
@app.route("/hands-on-1")
def hands_on_1():
    """Serve the single 'hands-on 1' page."""
    return render_template("hands-on-1.html")


@app.route("/about")
def about():
    """Serve the About page."""
    return render_template("about.html")


if __name__ == "__main__":
    ip = get_lan_ip()
    print(f" * Local:   http://127.0.0.1:{PORT}")
    print(f" * Network: http://{ip}:{PORT}")
    app.run(host=HOST, port=PORT)
