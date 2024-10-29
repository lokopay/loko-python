# ConfirmPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cryptocurrency** | [**CryptoCurrency**](CryptoCurrency.md) |  | [optional] 

## Example

```python
from loko_client.models.confirm_payment_request import ConfirmPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPaymentRequest from a JSON string
confirm_payment_request_instance = ConfirmPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmPaymentRequest.to_json())

# convert the object into a dict
confirm_payment_request_dict = confirm_payment_request_instance.to_dict()
# create an instance of ConfirmPaymentRequest from a dict
confirm_payment_request_from_dict = ConfirmPaymentRequest.from_dict(confirm_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


