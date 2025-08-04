from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import os

app = Flask(__name__)
app.secret_key = os.environ.get("LUNA_BLACKBOARD_SECRET", "dev_secret_DO_NOT_USE_IN_PROD")

shared_text = "Shared text here"

def get_password():
    pw_file = os.path.expanduser("~/.blackboard_pw")
    if os.path.exists(pw_file):
        with open(pw_file) as f:
            return f.read().strip()
    return os.environ.get("LUNA_BLACKBOARD_PASS", "changeme_1234")

PASSWORD = get_password()

@app.route("/", methods=["GET"])
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html", text=shared_text)

@app.route("/update", methods=["POST"])
def update():
    global shared_text
    if not session.get("logged_in"):
        return jsonify({"status": "not logged in"}), 403
    shared_text = request.json.get("text", "")
    return jsonify({"status": "ok"})

@app.route("/text")
def get_text():
    return jsonify({"text": shared_text})

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["pw"] == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5137)
