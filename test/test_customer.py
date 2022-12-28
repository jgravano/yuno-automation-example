from src.helpers.customer_helper import CustomerHelper
from src.requests.customers_requests import CustomersRequests


class TestCustomer:
    requests = CustomersRequests()
    helper = CustomerHelper()

    def test_create_customer_ok(self):
        """
        TEST: Se envía un post para crear un cliente, se espera obtener un status code 200.
        """
        response = self.requests.post_create_customer()
        assert response.status_code == 201
        assert response.json()['id'] is not None
        self.helper.assert_current_date(response)
        
    def test_get_customer(self):
        """
        TEST: se envía una petición con un customer especifico, debe devolver los datos de dicho customer.
        """
        response = self.requests.get_customer(id="fb74f0fb-a041-480a-ae12-c0d304ec9026")
        assert response.status_code == 200

    def test_get_invalid_customer(self):
        """
        TEST: se envía una petición con un customer inexistente, debe devolver error.
        """
        response = self.requests.get_customer(id="123123")
        assert response.status_code == 400
        assert response.json()['code'] == 'ILLEGAL_ARGUMENT'
        assert response.json()['messages'] == ['Illegal Argument']
