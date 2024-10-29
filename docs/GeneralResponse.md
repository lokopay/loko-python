# GeneralResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**message** | **str** |  | 
**token** | **str** |  | [optional] 

## Example

```python
from loko_client.models.general_response import GeneralResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralResponse from a JSON string
general_response_instance = GeneralResponse.from_json(json)
# print the JSON string representation of the object
print(GeneralResponse.to_json())

# convert the object into a dict
general_response_dict = general_response_instance.to_dict()
# create an instance of GeneralResponse from a dict
general_response_from_dict = GeneralResponse.from_dict(general_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


