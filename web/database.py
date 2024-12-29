from flask import session as flask_session
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TmplTableBase(Base):
    __abstract__ = True
    ins_user = Column(String, default=lambda: flask_session["user_id"] if "user_id" in flask_session else "system")
    ins_prg = Column(String, default=lambda: flask_session["screen_id"] if "screen_id" in flask_session else "web")
    ins_date = Column(DateTime, default=func.current_timestamp())
    upd_user = Column(String, default=lambda: flask_session["user_id"] if "user_id" in flask_session else "system", onupdate=lambda: flask_session["user_id"] if "user_id" in flask_session else "system")
    upd_prg = Column(String, default=lambda: flask_session["screen_id"] if "screen_id" in flask_session else "web", onupdate=lambda: flask_session["screen_id"] if "screen_id" in flask_session else "web")
    upd_date = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __repr__(self):
        return (
            f", ins_user={self.ins_user}, ins_prg={self.ins_prg}, ins_date={self.ins_date}"
            f", upd_user={self.upd_user}, upd_prg={self.upd_prg}, upd_date={self.upd_date}"
        )


DATABASE_URL = "postgresql+psycopg2://ucpadmin:ucpadmin@localhost/ucp_onlogi"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
db_session = Session()