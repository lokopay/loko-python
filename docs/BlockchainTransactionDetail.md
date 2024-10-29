# BlockchainTransactionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**tx_hash** | **str** |  | [optional] 
**confirmations** | **int** |  | [optional] 
**block_time** | **int** |  | [optional] 
**block_height** | **int** |  | [optional] 

## Example

```python
from loko_client.models.blockchain_transaction_detail import BlockchainTransactionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainTransactionDetail from a JSON string
blockchain_transaction_detail_instance = BlockchainTransactionDetail.from_json(json)
# print the JSON string representation of the object
print(BlockchainTransactionDetail.to_json())

# convert the object into a dict
blockchain_transaction_detail_dict = blockchain_transaction_detail_instance.to_dict()
# create an instance of BlockchainTransactionDetail from a dict
blockchain_transaction_detail_from_dict = BlockchainTransactionDetail.from_dict(blockchain_transaction_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


