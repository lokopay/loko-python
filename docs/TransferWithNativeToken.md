# TransferWithNativeToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**amount** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from loko_client.models.transfer_with_native_token import TransferWithNativeToken

# TODO update the JSON string below
json = "{}"
# create an instance of TransferWithNativeToken from a JSON string
transfer_with_native_token_instance = TransferWithNativeToken.from_json(json)
# print the JSON string representation of the object
print(TransferWithNativeToken.to_json())

# convert the object into a dict
transfer_with_native_token_dict = transfer_with_native_token_instance.to_dict()
# create an instance of TransferWithNativeToken from a dict
transfer_with_native_token_from_dict = TransferWithNativeToken.from_dict(transfer_with_native_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


