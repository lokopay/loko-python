# loko_client.NetworkfeesApi

All URIs are relative to *https://api.lokopay.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_fees**](NetworkfeesApi.md#get_network_fees) | **GET** /networkfees | Get network fees


# **get_network_fees**
> GetNetworkFees200Response get_network_fees()

Get network fees

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.get_network_fees200_response import GetNetworkFees200Response
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
    api_instance = loko_client.NetworkfeesApi(api_client)

    try:
        # Get network fees
        api_response = api_instance.get_network_fees()
        print("The response of NetworkfeesApi->get_network_fees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkfeesApi->get_network_fees: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNetworkFees200Response**](GetNetworkFees200Response.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return network fees |  * Access-Control-Expose-Headers -  <br>  * Content-Range -  <br>  |
**400** | returns error if request is invalid |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

