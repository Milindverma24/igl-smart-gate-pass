import random
from datetime import datetime

def generate_visitor_id():

    current_date = datetime.now().strftime(
        "%Y%m%d"
    )

    random_number = random.randint(
        1000,
        9999
    )

    return f"IGL-{current_date}-{random_number}"