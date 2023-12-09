from flask import Flask, Response, request, render_template, redirect, url_for
from sqlalchemy import exc

from crud_dz19 import add_users, get_user, create_user, get_all_users
from models_19 import create_table, drop_tables

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static-files/")

drop_tables()
create_table()
add_users()

@app.route("/",methods=["GET"])
def home_page_view():
    all_users = get_all_users()
    return render_template("home_dz19.html", users=all_users)

@app.route("/register", methods=["GET"])
def get_register_view():
    return render_template("register_dz19.html")


@app.route("/register", methods=["POST"])
def register_user_view():
    user_data = request.form
    try:
        user = create_user(
            username=user_data["username"],
            password=user_data["password"],
            email=user_data["email"]
        )
    except exc.IntegrityError:

        return f"""Пользователь с username: {user_data['username']}
         либо с email: {user_data['email']} уже существует"""

    return redirect(url_for("users_view", username=user.username))


@app.route("/<username>", methods=["GET"])
def users_view(username: str):


    try:
        user = get_user(username)
    except exc.NoResultFound:

        return Response("User not found.", status=404)

    return render_template(
        "user_dz19.html",
        username=user.username,
        email=user.email,
        password=user.password)
