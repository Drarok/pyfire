import json


def get_property_from_json_string(prop_name, json_string):
    return json.loads(json_string)[prop_name]