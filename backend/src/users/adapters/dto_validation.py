from flask import jsonify
import jsonschema
from jsonschema import validate

CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "password": {"type": "string"}
    },
    "required": ["email", "name", "age", "password"],
    "additionalProperties": False
}

def validate_dto(json_data, validation_schema):
        if not json_data:
            return jsonify({ "error": "Invalid JSON data"})    
        try:
            validate(instance=json_data, schema=validation_schema)    
        except jsonschema.ValidationError as e:
            return str(e)
        
        return None