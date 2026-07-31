from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Amazon Clone")
APP_ENV = os.getenv("APP_ENV", "Development")
APP_VERSION = os.getenv("APP_VERSION", "v1.0")

@app.route("/")
def home():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_env=APP_ENV,
        version=APP_VERSION,
        hostname=socket.gethostname()
    )

@app.route("/health")
def health():
    return {"status": "UP"}, 200

@app.route("/version")
def version():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)