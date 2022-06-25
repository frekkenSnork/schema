example = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://example.com/product.schema.json",
    "title": "Product",
    "description": "A product from Acme's catalog",
    "type": "object",
    "properties": {
        "dimensions": {
            "type": "object",
            "description": "3D dimentions",
            "properties": {                
                "sally": {"type": "number"},
                "polly": {"type": "number"},
            },
            "required": ["sally", "polly"],
        }
    },
    "required": ["productId", "productName", "price"],
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
number_schema = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "postcode", "huisnummer", "expired"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {"huisnummer": {"title": "home number", "type": "number"}},
}

mix = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "required": ["kenteken", "postcode", "huisnummer", "expired", "email"],
    "title": "Het objecttype Melding Openbare Ruimte",
    "properties": {
        "email": {"title": "Your email", "type": "string", "format": "email"},
        "huisnummer": {"title": "home number", "type": "number"}
    },
}