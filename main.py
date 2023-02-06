# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from schema_validator import SchemaValidate
from json_validators import save_schema,update_schema

class JsonSchemaValidation(object):
    def __init__(self):
        pass

    def validate_save(self):

        save_json = {
            "user_name": 23,
            "status": 1,
            "resolution": "Everything is OK. We should tune rule XYZ to reduce false-positives...",
            "origin": {"type": 1, "user":{"first_name":34}},
            "hypothesis": "Since the dawn of time, man has sought to exploit vulnerabilities",
            "entities": {},
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
                    },
                    "id": "sdf"
                }
            ],
            "evidence": [
                {
                    "event_id": "16696548011669654800000002016139259668",
                    "summary": "Malicious process example.exe downloaded a file on host my-computer",
                    "fields": ["process_name", "host", "file_hash"],
                    "iocs": [{"name": "IP", "value": "8.8.8.8"}],
                    "show_in_timeline": True,
                    "criticality": "Cti",
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

        resp = SchemaValidate(save_json, save_schema)

        print("resp:{}".format(resp))

    def validate_update(self):

        update_json = {
            "insert_id": 23,
            "status": 1,
            "resolution": "Everything is OK. We should tune rule XYZ to reduce false-positives...",
            "origin": {"type": 1, "user":{"first_name":34}},
            "entities": {}
        }

        resp = SchemaValidate(update_json, update_schema)

        print("resp:{}".format(resp))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jsonSchemaValidation = JsonSchemaValidation()

    jsonSchemaValidation.validate_save()

    #jsonSchemaValidation.validate_update()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
