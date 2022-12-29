from datetime import date

class AssertHelper:

    def assert_current_date(self, response):
        current_date = str(date.today())
        assert current_date in response.json()['created_at'], f'The current date is {current_date}'

   