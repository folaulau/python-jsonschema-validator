#######
# Copyright (C) 2019 Anvilogic Inc.
# Anvilogic CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Anvilogic Inc. is PROHIBITED
#######

save_evidence_schema = {
    "type": "object",
    "properties": {
        "type": { "type": "string" },
        "id": {
            "type": "number",
            "error_message": "origin.id is invalid. It must be an integer."
        },
        "criticality": {
            "type": "string",
            "enum": ["Critical", "Corresponding"]
        }
    },
    "required": ["id","criticality"]
}

save_schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "insert_id": {
            "type": "integer"
        },
        "title": {
            "type": "string",
            "minimum": 1,
            "error_message": "title is invalid"
        },
        "status": {
            "type": "string",
            "minLength": 1,
            "error_message": "status is invalid"
        },
        "hypothesis": {
            "type": "string",
            "minLength": 1,
            "error_message": "hypothesis is invalid"
        },
        "resolution": {
            "type": "string",
            "minLength": 1,
            "error_message": "resolution is invalid"
        },
        "origin": {
            "type": "object",
            "properties": {
                "type": { "type": "string" },
                "id": {
                    "type": "number",
                    "error_message": "origin.id is invalid"
                },
                "user": {
                    "type": "object",
                    "properties": {
                        "first_name": { "type": "string" },
                        "id": {
                            "type": "number",
                            "error_message": "origin.id is invalid"
                        }
                    },
                    "required": ["id"]
                },
            },
            "required": ["id","user"]
        },
        "entities": {
            "type": "array",
            "items": {
                "type": "object"
            },
            "error_message": "entities is invalid"
        },
        "queries": {
            "type": "array",
            "items": {
                "type": "object"
            }
        },
        "evidence": {
            "type": "array",
            "items": save_evidence_schema
        }
    },
    "required": ["title", "status", "hypothesis","origin","queries"],
    "if": {
        "properties": { "insert_id": { "pattern": "^\d+$" } }
    },
    "then": {
        "properties": { "hypothesis": { "pattern": ".*" } }
    }
}

update_schema = {
    "type": "object",
    "properties": {
        "insert_id": {
            "type": "integer"
        },
        "hypothesis": {
            "type": "string",
            "minLength": 1,
            "error_message": "hypothesis is invalid"
        },
        "resolution": {
            "type": "string",
            "minLength": 1,
            "error_message": "resolution is invalid"
        }
    },
    "if": {
        "properties": { "insert_id": { "pattern": "^\d+$" } }
    },
    "then": {
        "properties": { "hypothesis": { "pattern": ".*" } }
    }
}