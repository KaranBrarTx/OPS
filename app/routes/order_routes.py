from fastapi import FastAPI, HTTPException
from main import app

from schemas.order_schemas import Order
from services.order_services import (
    create_order_data,
    fetch_orders_data,
    cancel_order_data
)
from app.models.database import SessionLocal


@app.post("/orders")
def create_order(order: Order):
    db = SessionLocal()
    try:
        return create_order_data(db, order)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()


@app.get("/orders")
def fetch_orders():
    db = SessionLocal()
    try:
        return fetch_orders_data(db)
    finally:
        db.close()


@app.put("/orders/{order_id}/cancel")
def cancel_order(order_id: str):
    db = SessionLocal()
    try:
        order = cancel_order_data(db, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()