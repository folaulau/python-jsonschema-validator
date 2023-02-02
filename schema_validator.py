#######
# Copyright (C) 2019 Anvilogic Inc.
# Anvilogic CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Anvilogic Inc. is PROHIBITED
#######

# Python Imports
from jsonschema import Draft7Validator
from jsonschema._format import FormatChecker
from jsonschema.exceptions import ValidationError

def SchemaValidate(jsonData, schema):
    v = Draft7Validator(schema, format_checker=FormatChecker())

    validation_errors = [e for e in v.iter_errors(jsonData)]

    if len(validation_errors) == 0:
        return True

    errors = []

    for error in validation_errors:
        # print("error.schema_path={}".format(error.schema_path))
        # print("error.schema={}".format(error.schema))
        error_type = error.schema_path[-1]

        print("error_type={}, error.schema_path={}".format(error_type, error.schema_path))

        if error_type == "type":

            field_type = error.schema['type']

            message = ".".join(map(str, error.path))+" is not of type {}".format(field_type)
        elif error_type == "required":
            # print("error.schema={}".format(error.schema))
            # print("error.path={}".format(error.path))

            if len(error.path) != 0:
                message = ".".join(map(str, error.path)) +"."+((error.message).replace("'",""))
            else:
                message = ((error.message).replace("'",""))
        else:

            message = error.schema["error_message"] if 'error_message' in error.schema else error.message

        # error is an instance of jsonschema.exceptions.ValidationError

        errors.append(message)

        print("\n\n")

    result = errors if len(errors) > 1 else errors[0]

    return result

def get_error_field_name(error) -> str:
    pass