import os
from dotenv import load_dotenv
load_dotenv()

API_SECRET_KEY=os.getenv("API_SECRET_KEY")
API_PUBLIC_KEY=os.getenv("API_PUBLIC_KEY")

def default_headers(public_api_key=API_PUBLIC_KEY, private_secret_key=API_SECRET_KEY, x_idempotency_key=None):
    return {"accept": "application/json",
    "content-type": "application/json",
    "public-api-key": public_api_key,
    "private-secret-key":private_secret_key,
    "X-Idempotency-Key": x_idempotency_key
    } 