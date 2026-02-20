def load_data():
    pass

def fetch_product_data(product_id):
    data=load_data()

    if product_id in data:
        return data.get(product_id)
    
def create_product_data():
    pass