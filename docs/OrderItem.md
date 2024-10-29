# OrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**price** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**metadata** | **str** |  | [optional] 

## Example

```python
from loko_client.models.order_item import OrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItem from a JSON string
order_item_instance = OrderItem.from_json(json)
# print the JSON string representation of the object
print(OrderItem.to_json())

# convert the object into a dict
order_item_dict = order_item_instance.to_dict()
# create an instance of OrderItem from a dict
order_item_from_dict = OrderItem.from_dict(order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


