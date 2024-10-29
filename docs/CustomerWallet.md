# CustomerWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**object_secret** | **str** |  | [optional] 
**supported_cryptocurrencies** | [**List[CryptoCurrency]**](CryptoCurrency.md) |  | [optional] 
**customer** | [**PaymentCustomer**](PaymentCustomer.md) |  | [optional] 
**wallet_addresses** | [**List[WalletAddress]**](WalletAddress.md) |  | [optional] 

## Example

```python
from loko_client.models.customer_wallet import CustomerWallet

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerWallet from a JSON string
customer_wallet_instance = CustomerWallet.from_json(json)
# print the JSON string representation of the object
print(CustomerWallet.to_json())

# convert the object into a dict
customer_wallet_dict = customer_wallet_instance.to_dict()
# create an instance of CustomerWallet from a dict
customer_wallet_from_dict = CustomerWallet.from_dict(customer_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


