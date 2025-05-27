# CreatePaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**currency_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**customer** | [**PaymentCustomer**](PaymentCustomer.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 

## Example

```python
from loko_client.models.create_payment_request import CreatePaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentRequest from a JSON string
create_payment_request_instance = CreatePaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentRequest.to_json())

# convert the object into a dict
create_payment_request_dict = create_payment_request_instance.to_dict()
# create an instance of CreatePaymentRequest from a dict
create_payment_request_from_dict = CreatePaymentRequest.from_dict(create_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


