from flask import Blueprint, render_template

bp = Blueprint("menu", __name__)

@bp.get("/menu")
def get():
    return render_template("menu.html")