import loko_client
from loko_client.rest import ApiException
import sys
from pprint import pprint
import time

# Defining the host is optional and defaults to https://api.lokopay.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = loko_client.Configuration(
    host = "https://api-test.lokopay.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: publishableKeyAuth
configuration.api_key['publishableKeyAuth'] = "lkcEQtiMBW9n3BiSp76Mgfusxa0/U34HpFF72+5CYoU="
configuration.secret_key = "OEJBHA8DzwtFchFaO9iVF+xu40pm202XnE4yIJAPjzgqnsh9XamZWxsGJoKgahvAeiumvhyZYBSh564+YTKpWA=="

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['publishableKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with loko_client.ApiClient(configuration) as api_client:
    #payment process
    paymentApiInstance = loko_client.PaymentsApi(api_client)
    customer = loko_client.PaymentCustomer(id='test-xx-1')
    createPaymetRequest = loko_client.CreatePaymentRequest(
        customer=customer,
        amount = "1000",#充值10U, USDC的最小单位cents
        currency="USDC",
        # currency_type="fixed"
    )
    #1,create a payment
    print("start create payment")
    try:
        payment = paymentApiInstance.create_payment(createPaymetRequest)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_payment: %s\n" % e)
        sys.exit()


    #2,retrieve the payment for prices
    print("start retrieve payment for prices")
    start_time = time.time()
    while True:
        time.sleep(3)
        try:
            payment = paymentApiInstance.get_payment(id=payment.id,loko_object_secret=payment.obj_secret)
        except ApiException as e:
            print("Exception when calling PaymentsApi->get_payment: %s\n" % e)
            sys.exit()  
        if  len(payment.supported_cryptocurrencies)>0:
            break
        if time.time() - start_time > 30:
            print("get price over time")
            sys.exit()
    pickedCrypto = None
    for crypto_currency in payment.supported_cryptocurrencies:
        #选择以太坊网络的USDT币种
        if crypto_currency.network == "Ethereum"  and crypto_currency.price_pair == "USDT-USDC":
            pickedCrypto = crypto_currency  
            break 
    if pickedCrypto is None:
        print("no supported crypto currency")
        sys.exit()

    print(pickedCrypto)
    sys.exit()

    #3,confirm payment   
    print("start confirm payment")
    confirmPaymentRequest = loko_client.ConfirmPaymentRequest(cryptocurrency=pickedCrypto)
    try:    
        payment = paymentApiInstance.confirm_payment(id=payment.id,confirm_payment_request=confirmPaymentRequest) 
    except ApiException as e:
            print("Exception when calling PaymentsApi->confirm_payment: %s\n" % e)
            sys.exit()
    #4,retrieve the payment for deposit address   
    print("start retrieve payment for deposit address")     
    start_time = time.time()
    while True:
        time.sleep(3)
        try:
            payment = paymentApiInstance.get_payment(id=payment.id,loko_object_secret=payment.obj_secret)
        except ApiException as e:
            print("Exception when calling PaymentsApi->get_payment: %s\n" % e)
            sys.exit()  
        if  payment.currency_due_address != "":
            break
        if time.time() - start_time > 30:
            print("get deposited address over time")
            sys.exit()    
    print("deposited address:",payment.currency_due_address)         




    