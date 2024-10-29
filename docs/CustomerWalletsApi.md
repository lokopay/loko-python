# loko_client.CustomerWalletsApi

All URIs are relative to *https://api.lokopay.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_wallet**](CustomerWalletsApi.md#create_customer_wallet) | **POST** /customer_wallets | Create a customer wallet


# **create_customer_wallet**
> CustomerWallet create_customer_wallet(create_customer_wallet_request)

Create a customer wallet

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.create_customer_wallet_request import CreateCustomerWalletRequest
from loko_client.models.customer_wallet import CustomerWallet
from loko_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lokopay.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = loko_client.Configuration(
    host = "https://api.lokopay.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: publishableKeyAuth
configuration.api_key['publishableKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['publishableKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with loko_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = loko_client.CustomerWalletsApi(api_client)
    create_customer_wallet_request = loko_client.CreateCustomerWalletRequest() # CreateCustomerWalletRequest | 

    try:
        # Create a customer wallet
        api_response = api_instance.create_customer_wallet(create_customer_wallet_request)
        print("The response of CustomerWalletsApi->create_customer_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerWalletsApi->create_customer_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_customer_wallet_request** | [**CreateCustomerWalletRequest**](CreateCustomerWalletRequest.md)|  | 

### Return type

[**CustomerWallet**](CustomerWallet.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful create customer wallet |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

