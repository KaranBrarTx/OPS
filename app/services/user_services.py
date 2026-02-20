def load_data():
    pass



def fetch_user_data(user_id):
    data=load_data()
    if user_id in data:
        return data.get(user_id)
    

def create_user_data():
    pass