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

from loko_client.models.blockchain_transaction_detail import BlockchainTransactionDetail

class TestBlockchainTransactionDetail(unittest.TestCase):
    """BlockchainTransactionDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BlockchainTransactionDetail:
        """Test BlockchainTransactionDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BlockchainTransactionDetail`
        """
        model = BlockchainTransactionDetail()
        if include_optional:
            return BlockchainTransactionDetail(
                id = '',
                amount = '',
                currency = '',
                network = '',
                address = '',
                tx_hash = '',
                confirmations = 56,
                block_time = 56,
                block_height = 56
            )
        else:
            return BlockchainTransactionDetail(
        )
        """

    def testBlockchainTransactionDetail(self):
        """Test BlockchainTransactionDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
