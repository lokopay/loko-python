# ConfirmPayoutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_network_details** | [**List[DestinationNetworkDetail]**](DestinationNetworkDetail.md) |  | [optional] 

## Example

```python
from loko_client.models.confirm_payout_request import ConfirmPayoutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPayoutRequest from a JSON string
confirm_payout_request_instance = ConfirmPayoutRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmPayoutRequest.to_json())

# convert the object into a dict
confirm_payout_request_dict = confirm_payout_request_instance.to_dict()
# create an instance of ConfirmPayoutRequest from a dict
confirm_payout_request_from_dict = ConfirmPayoutRequest.from_dict(confirm_payout_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


