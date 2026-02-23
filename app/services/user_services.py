from app.models.user_model import User
from app.utils.id_generator import generate_id
def create_user_data(db,user):
    new_user=User(**user.model_dump(exclude={'id'}))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def fetch_user_data(db,user_id):
    return db.query(User).filter(User.id==user_id).first()

def fetch_all_data(db,user):
    return db.query(User).all()