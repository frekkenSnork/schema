schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "postcode", "huisnummer", "expired"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "kenteken": {
            "title": "Kenteken",
            "type": "string",
            # "format": "date",
            "pattern": "^[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?$",
            "description": "Kenteken van het voertuig waarvoor de aanvraag wordt gedaan.",
            "examples": ["XX-11-YY"],
        },
        # "expired":{
        #     "title": "Expired term",
        #     "type": "string",
        #     "format": "date",
        #     "description": "Term",
        # },
        # "address":{
        #     "title":"address",
        #      "type":"string",
        #      "pattern":"^[a-zA-Z]"
        # }
    },
}

form_io = {
    "components": [
        {
            "label": "Kenteken",
            "description": "Kenteken van het voertuig waarvoor de aanvraag wordt gedaan.",
            "tableView": True,
            "validate": {
                "required": True,
                "pattern": "^[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?-[A-Z0-9][A-Z0-9]?[A-Z0-9]?$",
            },
            "key": "kenteken",
            "type": "textfield",
            "input": True,
        },
    ]
}


if __name__ == "__main__":
    pass
