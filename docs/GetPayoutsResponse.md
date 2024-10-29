# GetPayoutsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**starting_after** | **str** |  | [optional] 
**ending_before** | **str** |  | [optional] 
**data** | [**List[Payout]**](Payout.md) |  | [optional] 

## Example

```python
from loko_client.models.get_payouts_response import GetPayoutsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayoutsResponse from a JSON string
get_payouts_response_instance = GetPayoutsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPayoutsResponse.to_json())

# convert the object into a dict
get_payouts_response_dict = get_payouts_response_instance.to_dict()
# create an instance of GetPayoutsResponse from a dict
get_payouts_response_from_dict = GetPayoutsResponse.from_dict(get_payouts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


