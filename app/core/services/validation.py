import re

def validate_required_fields(*args):
    if any(arg is None or arg == '' for arg in args):
        raise ValueError("All fields must be filled in")

def validate_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None