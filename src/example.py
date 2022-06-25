day_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "expired"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "expired": {
            "title": "End",
            "type": "string",
            "format": "date",
            "description": "Date of expire",
        }
    },
}
time_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": [],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "lunch": {
            "title": "My be lunch?",
            "type": "string",
            "format": "time",
            "description": "To lunch or not to lunch",
            "default": "11:30",
        }
    },
}
date_time_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": [],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "birthday": {
            "title": "Birthday",
            "type": "string",
            "format": "date-time",
            "description": "Are you really sure you remember it?",
            "default": "1900-00-00,11:30",
        }
    },
}
text_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "postcode", "huisnummer", "expired"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "kenteken": {
            "title": "Kenteken",
            "type": "string",
            "pattern": "^[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?$",
            "description": "Kenteken van het voertuig waarvoor de aanvraag wordt gedaan.",
            "maxLength": 250,
            "examples": ["XX-11-YY"],
        }
    },
}
textarea_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "postcode", "huisnummer", "expired"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "kenteken": {
            "title": "Kenteken",
            "type": "string",
            "pattern": "^[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?$",
            "description": "Kenteken van het voertuig waarvoor de aanvraag wordt gedaan.",
            "examples": ["XX-11-YY"],
        }
    },
}
number_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "postcode", "huisnummer", "expired"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {"huisnummer": {"title": "home number", "type": "number"}},
}
email_shema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "postcode", "huisnummer", "expired", "email"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "email": {"title": "Your email", "type": "string", "format": "email"}
    },

}

myobj2 = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "person data for nobody",
    "type": "object",
    "properties": {
        "user": {
            "type": "object",
            "title": "User data",
            "properties": {"name": {"title": "Your name", "type": "string"}},
            "required": ["name"],
        },
    },
    "required": ["user"],
}

myobj = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "person data for nobody",
    "properties": {
        "user": {
            "type": "object",
            "title": "Explore my object",
            "properties": {
                "name": {"title": "Your name", "type": "string"},
                "email": {"title": "your mail", "type": "string", "format": "email"},
            },
            "required": ["name", "email"],
        }
    },
    "required": ["user"],
}

nest = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "$id": "https://example.com/employee.schema.json",
    "title": "Record of employee",
    "description": "This document records the details of an employee",
    "title": "Person data",
    "properties": {
        "hobbies": {
            "description": "Hobbies of the employee",
            "type": "object",
            "properties": {
                "indoor": {
                    "type": "array",
                    "items": {
                        "description": "List of indoor hobbies",
                        "type": "string",
                    },
                },
                "outdoor": {
                    "type": "array",
                    "items": {
                        "description": "List of outdoor hobbies",
                        "type": "string",
                    },
                },
            },
        },
        "id": {"description": "A unique identifier for an employee", "type": "number"},
        "name": {"description": "Full name of the employee", "type": "string"},
        "age": {"description": "Age of the employee", "type": "number"},
    },
}


# FOO = {'components':
# [{
#     'legend': 'DIMENSIONS',
# 'key': 'fieldset',
# 'label': 'Field Set',
# 'type': 'fieldset',
# 'input': False,
# 'components': [],
# }
# ]}


if __name__ == "__main__":
    pass
