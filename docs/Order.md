# Order


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) |  | [optional] 
**subtotal** | **int** |  | [optional] 
**sales_tax** | **int** |  | [optional] 
**discount** | **int** |  | [optional] 
**shipping** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from loko_client.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


