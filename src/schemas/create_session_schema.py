import json
from dotenv import load_dotenv
import os
load_dotenv()

def create_session_body():
    return json.dumps({
    "amount": {
        "currency": "ARS",
        "value": 100
    },
    "customer_id": "fb74f0fb-a041-480a-ae12-c0d304ec9026",
    "merchant_order_id": "1234",
    "payment_description": "test",
    "country": "AR",
    "account_id": os.getenv("ACCOUNT_ID")
})