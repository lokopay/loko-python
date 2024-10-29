# CryptoCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**price_pair** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from loko_client.models.crypto_currency import CryptoCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoCurrency from a JSON string
crypto_currency_instance = CryptoCurrency.from_json(json)
# print the JSON string representation of the object
print(CryptoCurrency.to_json())

# convert the object into a dict
crypto_currency_dict = crypto_currency_instance.to_dict()
# create an instance of CryptoCurrency from a dict
crypto_currency_from_dict = CryptoCurrency.from_dict(crypto_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


