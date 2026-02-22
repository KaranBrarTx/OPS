from app.models.product_model import Product
from app.utils.id_generator import generate_id
def create_product_data(db,product):
    new_product=Product(
        id=generate_id(),**product.model_dump()

    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def fetch_product_data(db,product_id):
    return db.query(Product).filter(Product.id==product_id).first()