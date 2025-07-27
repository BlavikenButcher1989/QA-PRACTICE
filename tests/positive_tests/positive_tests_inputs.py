import pytest
from pages.inputs_page import TextInput
from pages.inputs_page import EmailField
from pages.inputs_page import PasswordField

from data.positive_data.positive_data_inputs import text_input_data_positive, email_field_data_positive, password_field_data_positive

class TestsInputsPositive:

    class TestTextInput:
        def test_text_input_required_field(self, driver):
            text_input_page = TextInput(driver)
            text_input_page.open_site()
            validation_message, required_field, error = text_input_page.check_text_input_is_required_field()
            assert validation_message == 'Заполните это поле.', 'Validation message does not exist'
            assert required_field == 'true', 'Attribute "Required" does not exist'
            assert error == 'This field is required.'

        @pytest.mark.parametrize('string', text_input_data_positive)
        def test_enter_text_into_field_valid(self, driver, string):
            text_input_page = TextInput(driver)
            text_input_page.open_site()
            text_result = text_input_page.check_enter_text_into_field_valid(string)
            assert string == text_result, 'Input text does not match with result text'

    class TestEmailField:

        def test_email_field_required_field(self, driver):
            email_field_page = EmailField(driver)
            email_field_page.open_site()
            validation_message, required_field, error = email_field_page.check_email_field_is_required_field()
            assert validation_message == 'Заполните это поле.', 'Validation message does not exist'
            assert required_field == 'true', 'Attribute "Required" does not exist'
            assert error == 'This field is required.'

        @pytest.mark.parametrize('string', email_field_data_positive)
        def test_enter_email_into_field_valid(self, driver, string):
            email_field_page = EmailField(driver)
            email_field_page.open_site()
            email_text_result = email_field_page.check_enter_email_into_field_valid(string)
            assert string == email_text_result, 'Email does not match with result text'


    class TestPasswordField:

        def test_password_field_required_field(self, driver):
            pass_field_page = PasswordField(driver)
            pass_field_page.open_site()
            validation_message, required_field, error = pass_field_page.check_password_field_is_required_field()
            assert validation_message == 'Заполните это поле.', 'Validation message does not exist'
            assert required_field == 'true', 'Attribute "Required" does not exist'
            assert error == 'This field is required.'

        @pytest.mark.parametrize('string', password_field_data_positive)
        def test_enter_password_into_field_valid(self, driver, string):
            pass_field_page = PasswordField(driver)
            pass_field_page.open_site()
            pass_text_result = pass_field_page.check_enter_password_into_field_valid(string)
            assert string == pass_text_result, 'Password does not match with result text'