import json
import random

def create_customer_body():
    return json.dumps({
    "document": {"document_number": "3094813"},
    "phone": {
        "country_code": "54",
        "number": "1135466332"
    },
    "billing_address": {
        "address_line_1": "CALLE",
        "city": "CITY",
        "country": "AR"
    },
    "shipping_address": {
        "address_line_1": "CALLE",
        "city": "CITY",
        "country": "AR"
    },
    "merchant_customer_id": str(random.random()),
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1990-02-28",
    "email": "johndoe@example.com",
    "nationality": "AR",
    "country": "AR"
})