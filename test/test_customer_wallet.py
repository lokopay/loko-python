# coding: utf-8

"""
    LokoPay API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2024-08-22
    Contact: dev@lokopay.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from loko_client.models.customer_wallet import CustomerWallet

class TestCustomerWallet(unittest.TestCase):
    """CustomerWallet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerWallet:
        """Test CustomerWallet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerWallet`
        """
        model = CustomerWallet()
        if include_optional:
            return CustomerWallet(
                id = '',
                object = '',
                object_secret = '',
                supported_cryptocurrencies = [
                    loko_client.models.crypto_currency.CryptoCurrency(
                        id = '', 
                        network = '', 
                        price = 1.337, 
                        price_pair = '', 
                        amount = '', 
                        currency = '', 
                        description = '', )
                    ],
                customer = loko_client.models.payment_customer.PaymentCustomer(
                    id = '', 
                    email = '', 
                    ip_address = '', 
                    destination_address = '', 
                    destination_network = '', 
                    destination_currency = '', ),
                wallet_addresses = [
                    loko_client.models.wallet_address.WalletAddress(
                        id = '', 
                        address = '', 
                        address_currency = '', 
                        address_network = '', 
                        description = '', )
                    ]
            )
        else:
            return CustomerWallet(
        )
        """

    def testCustomerWallet(self):
        """Test CustomerWallet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
