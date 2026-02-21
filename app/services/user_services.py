from app.models.user_model import User
from app.utils.id_generator import generate_id
def create_user_data(db,user):
    new_user=User(
        id=generate_id(),
        **user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def fetch_user_data(db,user_id):
    return db.query(User).filter(User.id==user_id).first()