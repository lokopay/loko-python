# loko_client.PayoutsApi

All URIs are relative to *https://api.lokopay.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_payout**](PayoutsApi.md#cancel_payout) | **POST** /payouts/{id}/cancel | Cancel payout
[**confirm_payout**](PayoutsApi.md#confirm_payout) | **POST** /payouts/{id}/confirm | Confirm payout
[**create_payout**](PayoutsApi.md#create_payout) | **POST** /payouts | Create a payout
[**get_payout**](PayoutsApi.md#get_payout) | **GET** /payouts/{id} | Get payout detail
[**get_payouts**](PayoutsApi.md#get_payouts) | **GET** /payouts | Get payouts


# **cancel_payout**
> Payout cancel_payout(id)

Cancel payout

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.payout import Payout
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
    api_instance = loko_client.PayoutsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel payout
        api_response = api_instance.cancel_payout(id)
        print("The response of PayoutsApi->cancel_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->cancel_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Payout**](Payout.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful cancel payout |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_payout**
> Payout confirm_payout(id, confirm_payout_request)

Confirm payout

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.confirm_payout_request import ConfirmPayoutRequest
from loko_client.models.payout import Payout
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
    api_instance = loko_client.PayoutsApi(api_client)
    id = 'id_example' # str | 
    confirm_payout_request = loko_client.ConfirmPayoutRequest() # ConfirmPayoutRequest | 

    try:
        # Confirm payout
        api_response = api_instance.confirm_payout(id, confirm_payout_request)
        print("The response of PayoutsApi->confirm_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->confirm_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **confirm_payout_request** | [**ConfirmPayoutRequest**](ConfirmPayoutRequest.md)|  | 

### Return type

[**Payout**](Payout.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful confirm payout |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payout**
> Payout create_payout(create_pout_request)

Create a payout

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.create_payout_request import CreatePayoutRequest
from loko_client.models.payout import Payout
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
    api_instance = loko_client.PayoutsApi(api_client)
    create_pout_request = loko_client.CreatePayoutRequest() # CreatePayoutRequest | 

    try:
        # Create a payout
        api_response = api_instance.create_payout(create_pout_request)
        print("The response of PayoutsApi->create_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->create_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pout_request** | [**CreatePayoutRequest**](CreatePayoutRequest.md)|  | 

### Return type

[**Payout**](Payout.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful create payout |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout**
> Payout get_payout(id, loko_object_secret=loko_object_secret)

Get payout detail

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.payout import Payout
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
    api_instance = loko_client.PayoutsApi(api_client)
    id = 'id_example' # str | 
    loko_object_secret = 'loko_object_secret_example' # str |  (optional)

    try:
        # Get payout detail
        api_response = api_instance.get_payout(id, loko_object_secret=loko_object_secret)
        print("The response of PayoutsApi->get_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->get_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **loko_object_secret** | **str**|  | [optional] 

### Return type

[**Payout**](Payout.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return payout objects |  * Access-Control-Expose-Headers -  <br>  * Content-Range -  <br>  |
**400** | returns error if request is invalid |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payouts**
> GetPayoutsResponse get_payouts(starting_after=starting_after, ending_before=ending_before, created_from=created_from, created_to=created_to, limit=limit, loko_object_secret=loko_object_secret, completed_from=completed_from, completed_to=completed_to, status=status)

Get payouts

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.get_payouts_response import GetPayoutsResponse
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
    api_instance = loko_client.PayoutsApi(api_client)
    starting_after = 'starting_after_example' # str |  (optional)
    ending_before = 'ending_before_example' # str |  (optional)
    created_from = 56 # int |  (optional)
    created_to = 56 # int |  (optional)
    limit = 10 # int |  (optional) (default to 10)
    loko_object_secret = 'loko_object_secret_example' # str |  (optional)
    completed_from = 56 # int |  (optional)
    completed_to = 56 # int |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # Get payouts
        api_response = api_instance.get_payouts(starting_after=starting_after, ending_before=ending_before, created_from=created_from, created_to=created_to, limit=limit, loko_object_secret=loko_object_secret, completed_from=completed_from, completed_to=completed_to, status=status)
        print("The response of PayoutsApi->get_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->get_payouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 
 **created_from** | **int**|  | [optional] 
 **created_to** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **loko_object_secret** | **str**|  | [optional] 
 **completed_from** | **int**|  | [optional] 
 **completed_to** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**GetPayoutsResponse**](GetPayoutsResponse.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return payout objects |  * Access-Control-Expose-Headers -  <br>  * Content-Range -  <br>  |
**400** | returns error if request is invalid |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

