import uuid
def generate_id()->str:
    unique_id=uuid.uuid4().hex[:8]
    return unique_id


