from src.helpers.assert_helper import AssertHelper
from src.requests.session_requests import SessionRequests


class TestCustomer:
    requests = SessionRequests()
    helper = AssertHelper()

    def test_create_session_ok(self):
        """
        TEST: Se envía un post para crear una session, se espera obtener un status code 200.
        """
        response = self.requests.post_create_session()
        assert response.status_code == 200
        assert response.json()['checkout_session'] is not None
        self.helper.assert_current_date(response)
        
    def test_get_session(self):
        """
        TEST: se envía una petición con una session, debe devolver los datos de dicha session.
        """
        response = self.requests.get_session(session_id="218852f7-7fd3-4f4e-b5af-777b2c5e683c")
        assert response.status_code == 200

    def test_get_invalid_session(self):
        """
        TEST: se envía una petición con una session inexistente, debe devolver error.
        """
        response = self.requests.get_session(session_id="218852f7-7fd3-4f4e-b6af-777b2c5e683c")
        assert response.status_code == 400
        assert response.json()['code'] == 'CHECKOUT_SESSION_NOT_EXISTS'
