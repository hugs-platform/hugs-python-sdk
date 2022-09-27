# coding: utf-8

"""
    Hugs Platform - OpenAPI 3.0

    The Hugs Platform API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ReviewResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "createdAt",
            "approved",
            "reviewerId",
        }
        
        class properties:
            reviewerId = schemas.StrSchema
            approved = schemas.BoolSchema
            createdAt = schemas.StrSchema
            __annotations__ = {
                "reviewerId": reviewerId,
                "approved": approved,
                "createdAt": createdAt,
            }
    
    createdAt: MetaOapg.properties.createdAt
    approved: MetaOapg.properties.approved
    reviewerId: MetaOapg.properties.reviewerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reviewerId"]) -> MetaOapg.properties.reviewerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approved"]) -> MetaOapg.properties.approved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["reviewerId", "approved", "createdAt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reviewerId"]) -> MetaOapg.properties.reviewerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approved"]) -> MetaOapg.properties.approved: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["reviewerId", "approved", "createdAt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, ],
        approved: typing.Union[MetaOapg.properties.approved, bool, ],
        reviewerId: typing.Union[MetaOapg.properties.reviewerId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReviewResponse':
        return super().__new__(
            cls,
            *args,
            createdAt=createdAt,
            approved=approved,
            reviewerId=reviewerId,
            _configuration=_configuration,
            **kwargs,
        )
