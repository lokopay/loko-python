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

from loko_client.models.create_payment_request import CreatePaymentRequest

class TestCreatePaymentRequest(unittest.TestCase):
    """CreatePaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePaymentRequest:
        """Test CreatePaymentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePaymentRequest`
        """
        model = CreatePaymentRequest()
        if include_optional:
            return CreatePaymentRequest(
                amount = '',
                currency = '',
                description = '',
                customer = loko_client.models.payment_customer.PaymentCustomer(
                    id = '', 
                    email = '', 
                    ip_address = '', 
                    destination_address = '', 
                    destination_network = '', 
                    destination_currency = '', ),
                order = loko_client.models.order.Order(
                    order_id = '', 
                    name = '', 
                    items = [
                        loko_client.models.order_item.OrderItem(
                            name = '', 
                            price = 56, 
                            currency = '', 
                            quantity = 56, 
                            metadata = '', )
                        ], 
                    subtotal = 56, 
                    sales_tax = 56, 
                    discount = 56, 
                    shipping = 56, 
                    total = 56, 
                    currency = '', )
            )
        else:
            return CreatePaymentRequest(
        )
        """

    def testCreatePaymentRequest(self):
        """Test CreatePaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()