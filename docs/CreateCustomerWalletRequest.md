# CreateCustomerWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) for FIAT, three or four letter code for cryptocurrencies. Cryptocurrency code list | [optional] 
**network** | **str** | The cryptocurrency network | [optional] 
**customer** | [**PaymentCustomer**](PaymentCustomer.md) |  | [optional] 

## Example

```python
from loko_client.models.create_customer_wallet_request import CreateCustomerWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerWalletRequest from a JSON string
create_customer_wallet_request_instance = CreateCustomerWalletRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerWalletRequest.to_json())

# convert the object into a dict
create_customer_wallet_request_dict = create_customer_wallet_request_instance.to_dict()
# create an instance of CreateCustomerWalletRequest from a dict
create_customer_wallet_request_from_dict = CreateCustomerWalletRequest.from_dict(create_customer_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


