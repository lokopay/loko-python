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
from loko_client.models.destination_network_detail import DestinationNetworkDetail
from typing import Optional, Set
from typing_extensions import Self

class GetNetworkFees200Response(BaseModel):
    """
    GetNetworkFees200Response
    """ # noqa: E501
    object: Optional[StrictStr] = None
    destination_network_details: Optional[List[DestinationNetworkDetail]] = None
    __properties: ClassVar[List[str]] = ["object", "destination_network_details"]

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
        """Create an instance of GetNetworkFees200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in destination_network_details (list)
        _items = []
        if self.destination_network_details:
            for _item_destination_network_details in self.destination_network_details:
                if _item_destination_network_details:
                    _items.append(_item_destination_network_details.to_dict())
            _dict['destination_network_details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetNetworkFees200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object"),
            "destination_network_details": [DestinationNetworkDetail.from_dict(_item) for _item in obj["destination_network_details"]] if obj.get("destination_network_details") is not None else None
        })
        return _obj


