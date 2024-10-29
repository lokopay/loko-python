# coding: utf-8

"""
    LokoPay API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2024-08-22
    Contact: dev@lokopay.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DestinationNetworkDetail(BaseModel):
    """
    DestinationNetworkDetail
    """ # noqa: E501
    id: Optional[StrictStr] = None
    destination_amount: Optional[StrictStr] = None
    destination_currency: Optional[StrictStr] = None
    destination_network: Optional[StrictStr] = None
    destination_network_description: Optional[StrictStr] = None
    destination_transaction_fee: Optional[StrictStr] = None
    destination_transaction_fee_currency: Optional[StrictStr] = None
    destination_network_fee: Optional[StrictStr] = None
    destination_network_fee_currency: Optional[StrictStr] = None
    destination_network_fee_monetary: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "destination_amount", "destination_currency", "destination_network", "destination_network_description", "destination_transaction_fee", "destination_transaction_fee_currency", "destination_network_fee", "destination_network_fee_currency", "destination_network_fee_monetary"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DestinationNetworkDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DestinationNetworkDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "destination_amount": obj.get("destination_amount"),
            "destination_currency": obj.get("destination_currency"),
            "destination_network": obj.get("destination_network"),
            "destination_network_description": obj.get("destination_network_description"),
            "destination_transaction_fee": obj.get("destination_transaction_fee"),
            "destination_transaction_fee_currency": obj.get("destination_transaction_fee_currency"),
            "destination_network_fee": obj.get("destination_network_fee"),
            "destination_network_fee_currency": obj.get("destination_network_fee_currency"),
            "destination_network_fee_monetary": obj.get("destination_network_fee_monetary")
        })
        return _obj

