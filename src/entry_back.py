import json
from factory import FieldFactory
from example import nest, myobj2
from example2 import example


def get_single_item(content: dict) -> dict:
    """create a new object depending on type of a field"""
    obj = FieldFactory.create(content=content)
    return obj


def convert_json_schema_to_py(json_schema: dict) -> dict:
    """
    reads json schema in json format and return dict of fields objects
    """
    properties = json_schema.get("properties", {})
    final_result = {"components": []}
    for key in properties.keys():
        object_flag = json_schema["properties"][key]["type"]
        content = properties[key]
        content.update({"key": key})
        # add check if key == "required" not present in JSON schema?
        if key in json_schema.get("required") and object_flag != "object":
            content.update({"required": True})
            single_field = get_single_item(content=properties[key])
            
        else:
            # need to drill nested properties
            # content["properties"] {'length': {'type': 'number'}, 'width': {'type': 'number'}, 'height': {'type': 'number'}}
            print("block object")  
            single_field = get_single_item(content=properties[key])    
            nested = content["properties"]           
            
           
                     
            # single_field.convert_json_schema_to_py(nested)


        
        # elem = json.dumps(single_field.dict_repr)
        # final_result["components"].append(json.loads(elem))
    print(single_field)
    # return final_result


print("final result", convert_json_schema_to_py(example))


"""
{'content': 
{'type': 'object', 
'description': '3D dimentions', 
'properties': 
    {
        'length': {'type': 'number'}, 
        'width': {'type': 'number'}, 
        'height': {'type': 'number'}
    }, 
'required': ['length', 'width', 'height'], 
'key': 'dimensions'
}
"""


if __name__ == "__main__":
    pass
