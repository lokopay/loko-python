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

from loko_client.models.confirm_payment_request import ConfirmPaymentRequest

class TestConfirmPaymentRequest(unittest.TestCase):
    """ConfirmPaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfirmPaymentRequest:
        """Test ConfirmPaymentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfirmPaymentRequest`
        """
        model = ConfirmPaymentRequest()
        if include_optional:
            return ConfirmPaymentRequest(
                cryptocurrency = loko_client.models.crypto_currency.CryptoCurrency(
                    id = '', 
                    network = '', 
                    price = 1.337, 
                    price_pair = '', 
                    amount = '', 
                    currency = '', 
                    description = '', )
            )
        else:
            return ConfirmPaymentRequest(
        )
        """

    def testConfirmPaymentRequest(self):
        """Test ConfirmPaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
