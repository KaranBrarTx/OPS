import json
from datetime import datetime

from app.models.order_model import Order
from app.models.product_model import Product
from app.models.user_model import User
from app.utils.id_generator import generate_id


def create_order_data(db, order):
    user=db.query(User).filter(User.id==order.user_id).first()
    if not user:
        raise Exception("User not found")

    total_amount=0
    items=order.items

    for item in items:
        product=db.query(Product).filter(
            Product.id==item["product_id"]
        ).first()

        if not product:
            raise Exception("Product not found")

        if product.stock_quantity<item["quantity"]:
            raise Exception("Insufficient stock")

        total_amount+=product.price*item["quantity"]

  
    for item in items:
        product=db.query(Product).filter(
            Product.id==item["product_id"]
        ).first()

        product.stock_quantity-=item["quantity"]

    new_order=Order(
        id=generate_id(),
        user_id=order.user_id,
        products=json.dumps(items),
        total_amount=total_amount,
        status="created",
        created_at=datetime.utcnow()
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


def fetch_orders_data(db):
    return db.query(Order).all()


def cancel_order_data(db, order_id):

    order=db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return None

    if order.status=="cancelled":
        raise Exception("Order already cancelled")

    items=json.loads(order.products)

    
    for item in items:
        product=db.query(Product).filter(
            Product.id==item["product_id"]
        ).first()

        if product:
            product.stock_quantity+=item["quantity"]

    order.status="cancelled"

    db.commit()
    db.refresh(order)

    return order