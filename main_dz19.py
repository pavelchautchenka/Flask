from flask import Flask, Response, request, render_template, redirect, url_for
from sqlalchemy import exc

from crud_dz19 import get_notes, create_notes, get_all_notes,add_notes
from models_19 import create_table, drop_tables

app = Flask(__name__,
            template_folder="templates",
            static_folder="static",
            static_url_path="/static-files/")

drop_tables()
create_table()
add_notes()


@app.route("/", methods=["GET"])
def home_page_view():
    all_notes = get_all_notes()
    return render_template("home_dz19.html", notes=all_notes)


@app.route("/register", methods=["GET"])
def get_register_view():
    return render_template("register_dz19.html")


@app.route("/register", methods=["POST"])
def register_note_view():
    note_data = request.form
    try:
        note = create_notes(
            title=note_data["title"],
            content=note_data["content"]
        )
    except exc.IntegrityError:

        return f"""Note with username: {note_data['title']}
         already existed"""

    return redirect(url_for("note_view", uuid=note.uuid))


@app.route("/<uuid>", methods=["GET"])
def note_view(uuid):


    try:
        note = get_notes(uuid)
    except exc.NoResultFound:

        return Response("Note not found.", status=404)

    return render_template(
        "note_dz19.html",
        uuid=note.uuid,
        title=note.title,
        content=note.content,
        created_at=note.created_at
        )
