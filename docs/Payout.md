# Payout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**customer** | [**PaymentCustomer**](PaymentCustomer.md) |  | [optional] 
**destination_network_details** | [**List[DestinationNetworkDetail]**](DestinationNetworkDetail.md) |  | [optional] 
**blockchain_transaction_details** | [**List[BlockchainTransactionDetail]**](BlockchainTransactionDetail.md) |  | [optional] 
**canceled_at** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**obj_secret** | **str** |  | [optional] 
**failed_reason** | **str** |  | [optional] 
**transfer_with_native_token** | [**TransferWithNativeToken**](TransferWithNativeToken.md) |  | [optional] 

## Example

```python
from loko_client.models.payout import Payout

# TODO update the JSON string below
json = "{}"
# create an instance of Payout from a JSON string
payout_instance = Payout.from_json(json)
# print the JSON string representation of the object
print(Payout.to_json())

# convert the object into a dict
payout_dict = payout_instance.to_dict()
# create an instance of Payout from a dict
payout_from_dict = Payout.from_dict(payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


