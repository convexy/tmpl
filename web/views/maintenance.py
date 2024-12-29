from flask import Blueprint, session as flask_session, render_template
from web.database import db_session
from web.models.m_usr import MUser

bp = Blueprint("maintenance", __name__)

@bp.get("/maintenance")
def get():
    flask_session["user_id"] = "admin500"
    flask_session["screen_id"] = "maintenance"
    users = db_session.query(MUser).all()
    users[0].area_code = "500"
    db_session.commit()
    return render_template("maintenance.html", users=users)

