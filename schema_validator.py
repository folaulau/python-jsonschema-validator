#######
# Copyright (C) 2019 Anvilogic Inc.
# Anvilogic CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Anvilogic Inc. is PROHIBITED
#######

# Python Imports
from jsonschema import Draft7Validator


def SchemaValidate(jsonData, schemaName):
    v = Draft7Validator(schemaName)
    validation_errors = [e for e in v.iter_errors(jsonData)]

    if len(validation_errors) == 0:
        return True

    errors = []

    for error in validation_errors:
        # error is an instance of jsonschema.exceptions.ValidationError
        message = error.schema["error_message"] if 'error_message' in error.schema else error.message
        errors.append(message)

    result = errors if len(errors) > 1 else errors[0]

    return result
