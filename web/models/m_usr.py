from sqlalchemy import Column, String
from web.database import TmplTableBase

class MUser(TmplTableBase):
    __tablename__ = "ucp_m_usr"

    user_id = Column(String, primary_key=True)
    user_name = Column(String, nullable=False)
    user_password = Column(String)
    user_group_id = Column(String)
    country_code = Column(String)
    area_code = Column(String)
    plant_code = Column(String)
    machine_no = Column(String)

    def __repr__(self):
        return (
            f"<MUsr(user_id={self.user_id}, user_name={self.user_name}, user_password={self.user_password}"
            f", user_group_id={self.user_group_id}, country_code={self.country_code}, area_code={self.area_code}"
            f", plant_code={self.plant_code}, machine_no={self.machine_no}"
            f", {super().__repr__()}"
        )