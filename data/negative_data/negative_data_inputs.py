# Text input data negative
text_input_data_negative = [
    "a",
    "x" * 26,
    "text with spaces",
    "text@mail",
    "text.123",
    "Текст",
    "日本語",
    r"a\tb",
    r"a\nb",
]

errors = [
    'Please enter 2 or more characters',
    'Please enter no more than 25 characters',
    'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
]

# Email field data negative
email_field_data_negative = [
    "plainstring",
    "user@",
    "@domain.com",
    "user@domain",
    "user@.com",
    "user@domain..com",
    "user@domain.com.",
    "user@-domain.com",
    "user@domain.c",
    "user@ localhost",
    "user@домен",
    "user@domain,com"
]

# Password field data negative
password_field_data_negative = [
    "short1!",
    "nouppercase1!",
    "NOLOWERCASE1!",
    "NoDigits!!",
    "Passw0rd",
    "password",
    "PASSWORD1",
    "12345678",
    "!@#$%^&*",
    "Пароль123!",
    "A1!",
]
