# PaymentCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**destination_address** | **str** |  | [optional] 
**destination_network** | **str** |  | [optional] 
**destination_currency** | **str** |  | [optional] 

## Example

```python
from loko_client.models.payment_customer import PaymentCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCustomer from a JSON string
payment_customer_instance = PaymentCustomer.from_json(json)
# print the JSON string representation of the object
print(PaymentCustomer.to_json())

# convert the object into a dict
payment_customer_dict = payment_customer_instance.to_dict()
# create an instance of PaymentCustomer from a dict
payment_customer_from_dict = PaymentCustomer.from_dict(payment_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


