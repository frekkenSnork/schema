import json
from factory import FieldFactory
# from example import nest, myobj2
from example2 import example,text_schema,number_schema,mix 


def get_single_item(content: dict) -> dict:
    """create a new object depending on type of a field"""
    obj = FieldFactory.create(content=content)
    return obj

def drill_object(data,required,single_field):
    json_schema = {"properties":data,"required":required}
    result = convert_json_schema_to_py(json_schema=json_schema)
    single_field.components.append(result)
    


def convert_json_schema_to_py(json_schema: dict) -> dict:
    """
    reads json schema in json format and return dict of fields objects
    """
    final_result = {"components": []}
    properties = json_schema.get("properties", {})    
    for key in properties.keys():
        object_flag = json_schema["properties"][key]["type"]
        content = properties[key]
        content.update({"key": key})
        # add check if key == "required" not present in JSON schema?
        if key in json_schema.get("required") and object_flag != "object":
            content.update({"required": True})
            single_field = get_single_item(content=properties[key])   
            elem = json.dumps(single_field.dict_repr)
            final_result["components"].append(json.loads(elem))         
        else:             
            single_field = get_single_item(content=properties[key])   
            data = content["properties"]
            required = content["required"]            
            drill_object(data,required,single_field=single_field) 
            # single_field.components.append(drill_object(data,required))                
            elem = json.dumps(single_field.dict_repr)
            final_result["components"].append(json.loads(elem))
            # print(single_field.__dict__)
    return final_result

           

print(convert_json_schema_to_py(example))
        
   
# def get_final_json(single_field):
#     final_result = {"components": []}
#     elem = json.dumps(single_field.dict_repr)
#     final_result["components"].append(json.loads(elem))
#     return final_result

# print("final result", convert_json_schema_to_py(example))


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
