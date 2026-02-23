import json
from datetime import datetime
from fastapi import HTTPException

from app.models.order_model import Order
from app.models.product_model import Product
from app.models.user_model import User
from app.utils.id_generator import generate_id


def create_order_data(db, order):

    user = db.query(User).filter(User.id == order.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    total_amount=0
    items = order.items
    products_cache=[]

    for item in items:
        product=db.query(Product).filter(
            Product.id==item.product_id
        ).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product.stock_quantity<item.quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        total_amount+=product.price*item.quantity
        products_cache.append((product,item.quantity))

    for product, quantity in products_cache:
        product.stock_quantity-=quantity

    items_json=json.dumps(
        [item.model_dump() for item in items]
    )

    new_order=Order(
        user_id=order.user_id,
        products=items_json,
        total_amount=total_amount,
        status="created"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


def fetch_orders_data(db):
    return db.query(Order).all()


def cancel_order_data(db, order_id):

    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.status == "cancelled":
        raise HTTPException(
            status_code=400,
            detail="Order already cancelled"
        )

    items = json.loads(order.products)

    for item in items:
        product = db.query(Product).filter(
            Product.id == item["product_id"]
        ).first()

        if product:
            product.stock_quantity += item["quantity"]
    order.status = "cancelled"

    db.commit()
    db.refresh(order)
    return order