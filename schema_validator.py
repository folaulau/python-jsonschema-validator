#######
# Copyright (C) 2019 Anvilogic Inc.
# Anvilogic CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Anvilogic Inc. is PROHIBITED
#######

# Python Imports
from jsonschema import Draft7Validator

def SchemaValidate(jsonData, schema):
    v = Draft7Validator(schema)

    validation_errors = [e for e in v.iter_errors(jsonData)]

    if len(validation_errors) == 0:
        return True

    errors = []

    for error in validation_errors:
        # print("error.schema_path={}".format(error.schema_path))
        # print("error.schema={}".format(error.schema))
        error_type = error.schema_path[-1]

        print("error.path={}, error.path.type={}, error_type={}, error.schema_path={}".format(error.path, type(error.path), error_type, error.schema_path))

        if error_type == "type" or error_type == "enum":

            message = ".".join(map(str, error.path)) + " value of {}".format(error.message)

        elif error_type == "required":
            # print("error.schema={}".format(error.schema))
            # print("error.path={}".format(error.path))

            # remove single quotes on field name
            message = ((error.message).replace("'", ""))

            if len(error.path) != 0:
                message = ".".join(map(str, error.path)) +"."+message

        else:

            message = error.schema["error_message"] if 'error_message' in error.schema else error.message

        # error is an instance of jsonschema.exceptions.ValidationError

        errors.append(message)

        print("\n\n")

    result = errors if len(errors) > 1 else errors[0]

    return result

def get_error_field_name(error) -> str:
    pass