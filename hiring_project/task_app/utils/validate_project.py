from datetime import date, datetime
import re


def check_is_str(value) -> bool:
    return True if isinstance(value, str) else False


def check_is_null(value) -> bool:
    return True if value == None or value == "" else False


def check_is_int(value) -> bool:
    if check_is_str(value):
        return True if value.isdigit() else False

    return True if isinstance(value, int) else False


def check_is_float(value) -> bool:
    if check_is_str(value):
        pattern = "^[-+]?[0-9]*\.?[0-9]+$"
        return bool(re.match(pattern, value))

    return True if isinstance(value, float) or check_is_int(value) \
        else False


def check_in_range(value, given_range) -> bool:
    value = value.lower() if check_is_str(value) else value
    return True if value in given_range else False


def check_is_date(value) -> bool:
    converted_value = datetime.strptime(value, "%Y-%m-%d").date()
    return True if isinstance(converted_value, date) else False
