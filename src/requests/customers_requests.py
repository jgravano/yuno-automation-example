import os
import src.api.endpoints as endpoints
import src.schemas.create_customer_schema as schema
from src.api.api_client import ApiClient
from dotenv import load_dotenv
load_dotenv()

class CustomersRequests:
    api_client = ApiClient(os.getenv("BASE_URL"))

    def post_create_customer(self):
        response = self.api_client.post(path=endpoints.CUSTOMERS, body=schema.create_customer_body())
        return response

    def get_customer(self, id):
        response = self.api_client.get(path=f'{endpoints.CUSTOMERS}/{id}')
        return response