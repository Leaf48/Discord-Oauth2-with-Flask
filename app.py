from flask import Flask, render_template, request, jsonify, redirect, session
from utils import get_token, get_user_guilds

app = Flask(__name__)
app.secret_key = "chinko"


@app.route("/")
def home():
    if "token" in session:
        return redirect("/dashboard")
    return render_template("index.html")


@app.route("/oauth/discord")
def oauth():
    token = get_token(request.args.get("code"))
    session["token"] = token
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    if "token" not in session:
        return redirect("https://discord.com/api/oauth2/authorize?client_id=974748075748917258&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Foauth%2Fdiscord&response_type=code&scope=identify%20guilds%20guilds.members.read")

    user_guilds = get_user_guilds(session["token"])

    for i in user_guilds:
        print(i["name"])

    return render_template("dashboard.html", guilds=user_guilds)


if __name__ == "__main__":
    app.run(debug=True)
