#######
# Copyright (C) 2019 Anvilogic Inc.
# Anvilogic CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Anvilogic Inc. is PROHIBITED
#######

save_schema = {
    "type": "object",
    "properties": {
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
            "items": {
                "type": "object"
            }
        }
    },
    "required": ["title", "status", "hypothesis","origin"]
}

save_json = {
    "title": "",
    "status": "test-status",
    "resolution": "Everything is OK. We should tune rule XYZ to reduce false-positives...",
    "origin": {"type": "ATD Insight", "id": 233},
    "hypothesis": "Since the dawn of time, man has sought to exploit vulnerabilities",
    "entities": [{"name": "test"}],
    "queries": [
        {
            "execution_date": "2023-01-21 18:28:35",
            "start_date": "2023-01-21 18:28:35",
            "end_date": "2023-01-21 18:28:35",
            "include": [{"name": "test"}, {"name": "test2"}],
            "exclude": [{"name": "test"}, {"name": "test2"}],
            "total_events": 23,
            "show_in_history": False,
            "entities": {
                "host": 23,
                "user": 123
            }
        }
    ],
    "evidence": [
        {
            "event_id": "16696548011669654800000002016139259668",
            "summary": "Malicious process example.exe downloaded a file on host my-computer",
            "fields": ["process_name", "host", "file_hash"],
            "iocs": [{"name": "IP", "value": "8.8.8.8"}],
            "show_in_timeline": True,
            "criticality": "CRITICAL",
            "notes": "test note"
        }
    ],
    "relationships": {
        "source_type": "event",
        "source_id": "string",
        "target_type": "entity",
        "target_id": "GUID",
        "title": "string",
        "note": "string"
    }
}