# loko_client.PaymentsApi

All URIs are relative to *https://api.lokopay.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_payment**](PaymentsApi.md#cancel_payment) | **POST** /payments/{id}/cancel | Cancel payment
[**confirm_payment**](PaymentsApi.md#confirm_payment) | **POST** /payments/{id}/confirm | Confirm payment
[**create_payment**](PaymentsApi.md#create_payment) | **POST** /payments | Create a payment
[**get_payment**](PaymentsApi.md#get_payment) | **GET** /payments/{id} | Get payment detail
[**get_payments**](PaymentsApi.md#get_payments) | **GET** /payments | Get payments
[**refund_payment**](PaymentsApi.md#refund_payment) | **POST** /payments/{id}/refund | Refund payment


# **cancel_payment**
> Payment cancel_payment(id)

Cancel payment

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.payment import Payment
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
    api_instance = loko_client.PaymentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel payment
        api_response = api_instance.cancel_payment(id)
        print("The response of PaymentsApi->cancel_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->cancel_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful cancel payment |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_payment**
> Payment confirm_payment(id, confirm_payment_request)

Confirm payment

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.confirm_payment_request import ConfirmPaymentRequest
from loko_client.models.payment import Payment
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
    api_instance = loko_client.PaymentsApi(api_client)
    id = 'id_example' # str | 
    confirm_payment_request = loko_client.ConfirmPaymentRequest() # ConfirmPaymentRequest | 

    try:
        # Confirm payment
        api_response = api_instance.confirm_payment(id, confirm_payment_request)
        print("The response of PaymentsApi->confirm_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->confirm_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **confirm_payment_request** | [**ConfirmPaymentRequest**](ConfirmPaymentRequest.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful confirm payment |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment**
> Payment create_payment(create_payment_request)

Create a payment

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.create_payment_request import CreatePaymentRequest
from loko_client.models.payment import Payment
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
    api_instance = loko_client.PaymentsApi(api_client)
    create_payment_request = loko_client.CreatePaymentRequest() # CreatePaymentRequest | 

    try:
        # Create a payment
        api_response = api_instance.create_payment(create_payment_request)
        print("The response of PaymentsApi->create_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->create_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_request** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful create payment |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> Payment get_payment(id, loko_object_secret=loko_object_secret)

Get payment detail

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.payment import Payment
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
    api_instance = loko_client.PaymentsApi(api_client)
    id = 'id_example' # str | 
    loko_object_secret = 'loko_object_secret_example' # str |  (optional)

    try:
        # Get payment detail
        api_response = api_instance.get_payment(id, loko_object_secret=loko_object_secret)
        print("The response of PaymentsApi->get_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **loko_object_secret** | **str**|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return payment objects |  * Access-Control-Expose-Headers -  <br>  * Content-Range -  <br>  |
**400** | returns error if request is invalid |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments**
> GetPaymentsResponse get_payments(starting_after=starting_after, ending_before=ending_before, created_from=created_from, created_to=created_to, completed_from=completed_from, completed_to=completed_to, status=status, limit=limit, loko_object_secret=loko_object_secret)

Get payments

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.get_payments_response import GetPaymentsResponse
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
    api_instance = loko_client.PaymentsApi(api_client)
    starting_after = 'starting_after_example' # str |  (optional)
    ending_before = 'ending_before_example' # str |  (optional)
    created_from = 56 # int |  (optional)
    created_to = 56 # int |  (optional)
    completed_from = 56 # int |  (optional)
    completed_to = 56 # int |  (optional)
    status = 'status_example' # str |  (optional)
    limit = 10 # int |  (optional) (default to 10)
    loko_object_secret = 'loko_object_secret_example' # str |  (optional)

    try:
        # Get payments
        api_response = api_instance.get_payments(starting_after=starting_after, ending_before=ending_before, created_from=created_from, created_to=created_to, completed_from=completed_from, completed_to=completed_to, status=status, limit=limit, loko_object_secret=loko_object_secret)
        print("The response of PaymentsApi->get_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_after** | **str**|  | [optional] 
 **ending_before** | **str**|  | [optional] 
 **created_from** | **int**|  | [optional] 
 **created_to** | **int**|  | [optional] 
 **completed_from** | **int**|  | [optional] 
 **completed_to** | **int**|  | [optional] 
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 10]
 **loko_object_secret** | **str**|  | [optional] 

### Return type

[**GetPaymentsResponse**](GetPaymentsResponse.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | return payment objects |  * Access-Control-Expose-Headers -  <br>  * Content-Range -  <br>  |
**400** | returns error if request is invalid |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_payment**
> Payment refund_payment(id)

Refund payment

### Example

* Api Key Authentication (publishableKeyAuth):

```python
import loko_client
from loko_client.models.payment import Payment
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
    api_instance = loko_client.PaymentsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Refund payment
        api_response = api_instance.refund_payment(id)
        print("The response of PaymentsApi->refund_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->refund_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[publishableKeyAuth](../README.md#publishableKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful refund payment |  -  |
**400** | returns error of invalid auth token is passed |  -  |
**401** | returns error of invalid auth token is passed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

