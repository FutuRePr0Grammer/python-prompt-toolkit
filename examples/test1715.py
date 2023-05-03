from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.validation import Validator


def is_number(text):
    return text.isdigit()


validator = Validator.from_callable(
    is_number,
    error_message='This input contains non-numeric characters')

age = input_dialog(title="Age", text="Your age:",
                   validator=validator).run()

print(f"Your age: {age}")
