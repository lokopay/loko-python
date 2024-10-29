# DestinationNetworkDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**destination_amount** | **str** |  | [optional] 
**destination_currency** | **str** |  | [optional] 
**destination_network** | **str** |  | [optional] 
**destination_network_description** | **str** |  | [optional] 
**destination_transaction_fee** | **str** |  | [optional] 
**destination_transaction_fee_currency** | **str** |  | [optional] 
**destination_network_fee** | **str** |  | [optional] 
**destination_network_fee_currency** | **str** |  | [optional] 
**destination_network_fee_monetary** | **str** |  | [optional] 

## Example

```python
from loko_client.models.destination_network_detail import DestinationNetworkDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationNetworkDetail from a JSON string
destination_network_detail_instance = DestinationNetworkDetail.from_json(json)
# print the JSON string representation of the object
print(DestinationNetworkDetail.to_json())

# convert the object into a dict
destination_network_detail_dict = destination_network_detail_instance.to_dict()
# create an instance of DestinationNetworkDetail from a dict
destination_network_detail_from_dict = DestinationNetworkDetail.from_dict(destination_network_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


