# GetNetworkFees200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**destination_network_details** | [**List[DestinationNetworkDetail]**](DestinationNetworkDetail.md) |  | [optional] 

## Example

```python
from loko_client.models.get_network_fees200_response import GetNetworkFees200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNetworkFees200Response from a JSON string
get_network_fees200_response_instance = GetNetworkFees200Response.from_json(json)
# print the JSON string representation of the object
print(GetNetworkFees200Response.to_json())

# convert the object into a dict
get_network_fees200_response_dict = get_network_fees200_response_instance.to_dict()
# create an instance of GetNetworkFees200Response from a dict
get_network_fees200_response_from_dict = GetNetworkFees200Response.from_dict(get_network_fees200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


