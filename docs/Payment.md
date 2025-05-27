# Payment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**currency_type** | **str** |  | [optional] 
**amount_paid** | **str** |  | [optional] 
**currency_paid** | **str** |  | [optional] 
**amount_due** | **str** |  | [optional] 
**currency_due** | **str** |  | [optional] 
**currency_due_network** | **str** |  | [optional] 
**currency_due_address** | **str** |  | [optional] 
**currency_due_address_only** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**customer** | [**PaymentCustomer**](PaymentCustomer.md) |  | [optional] 
**supported_cryptocurrencies** | [**List[CryptoCurrency]**](CryptoCurrency.md) |  | [optional] 
**blockchain_transaction_details** | [**List[BlockchainTransactionDetail]**](BlockchainTransactionDetail.md) |  | [optional] 
**price_expires_at** | **int** |  | [optional] 
**address_expires_at** | **int** |  | [optional] 
**expires_at** | **int** |  | [optional] 
**canceled_at** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**obj_secret** | **str** |  | [optional] 
**failed_reason** | **str** |  | [optional] 

## Example

```python
from loko_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


