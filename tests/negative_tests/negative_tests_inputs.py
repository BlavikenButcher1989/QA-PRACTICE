import pytest
from pages.inputs_page import TextInput
from pages.inputs_page import EmailField
from pages.inputs_page import PasswordField

from data.negative_data.negative_data_inputs import text_input_data_negative, errors, email_field_data_negative, password_field_data_negative

class TestsInputsNegative:

    class TestTextInput:

        @pytest.mark.parametrize('string', text_input_data_negative)
        def test_enter_text_into_field_invalid(self, driver, string):
            text_input_page = TextInput(driver)
            text_input_page.open_site()
            error = text_input_page.check_enter_text_into_field_invalid(string)
            assert error in errors, 'The field accept string'

    class TestEmailField:

        @pytest.mark.parametrize('string', email_field_data_negative)
        def test_enter_email_into_field_invalid(self, driver, string):
            email_field_page = EmailField(driver)
            email_field_page.open_site()
            error = email_field_page.check_enter_email_into_field_invalid(string)
            assert error == 'Enter a valid email address.', 'The field accept string'

    class TestPasswordField:

        @pytest.mark.parametrize('string', password_field_data_negative)
        def test_enter_password_into_field_invalid(self, driver, string):
            pass_field_page = PasswordField(driver)
            pass_field_page.open_site()
            error = pass_field_page.check_enter_password_into_field_invalid(string)
            assert error == 'Low password complexity', 'The field accept string'