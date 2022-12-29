import os
import src.api.endpoints as endpoints
import src.schemas.create_session_schema as schema
from src.api.api_client import ApiClient
from dotenv import load_dotenv
load_dotenv()

class SessionRequests:
    api_client = ApiClient(os.getenv("BASE_URL"))

    def post_create_session(self):
        response = self.api_client.post(path=endpoints.SESSIONS, body=schema.create_session_body())
        return response

    def get_session(self, session_id):
        response = self.api_client.get(path=f'{endpoints.SESSIONS}/{session_id}/{endpoints.PAYMENT_METHODS}')
        return response