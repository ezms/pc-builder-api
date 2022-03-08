from werkzeug.exceptions import BadRequest


def validate_body(payload: dict, **kwargs):

    types = {str: "string", int: "integer", bool: "boolean"}

    invalid_types = [
        f"{key}" for key, value in kwargs.items() if type(payload.get(key)) != value
    ]

    valid_types = [
        f"{key} type should be {types.get(value, value.__name__)}"
        for key, value in kwargs.items()
    ]

    missing_fields = [
        f"{key}" for key in kwargs.keys() if payload.get(key, None) == None
    ]

    if missing_fields:
        output_missing_fields = {
            "available_fields": list(kwargs.keys()),
            "missing_keys": missing_fields,
        }
        raise BadRequest(description=output_missing_fields)

    if invalid_types:
        output_invalid_types = {
            "available_fields": valid_types,
            "invalid_fields": invalid_types,
        }
        raise BadRequest(description=output_invalid_types)
