import loko_client
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
configuration.api_key['publishableKeyAuth'] = "owgX7UqW96sxaG/3KF6L+SzWy2kWPCcUm67tem+MDB4="
configuration.secret_key = "xSJ/2AteaZT4bEw5VY7bgJ6vImNJVdWqS0UtCZ9epZgs1KsiTE6CKwmiGnj2v6b/MWo9vnBxJVLEyQn/IRSX5A=="

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['publishableKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with loko_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = loko_client.CustomerWalletsApi(api_client)
    create_customer_wallet_request = loko_client.CreateCustomerWalletRequest(
        currency='ETH',
        network='Ethereum',
        customer=loko_client.PaymentCustomer(
            id='xxxx',
            email='',
            ip_address='',
            destination_address='',
            destination_network='',
            destination_currency='', )
    ) # CreateCustomerWalletRequest |
    try:
        # Create a customer wallet
        api_response = api_instance.create_customer_wallet(create_customer_wallet_request)
        print("The response of CustomerWalletsApi->create_customer_wallet:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerWalletsApi->create_customer_wallet: %s\n" % e)