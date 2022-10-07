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


class ContributionRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "contributionType",
            "appId",
            "contributionData",
        }
        
        class properties:
            appId = schemas.StrSchema
            contributionType = schemas.StrSchema
            contributionData = schemas.DictSchema
            contributionGroup = schemas.StrSchema
            __annotations__ = {
                "appId": appId,
                "contributionType": contributionType,
                "contributionData": contributionData,
                "contributionGroup": contributionGroup,
            }
    
    contributionType: MetaOapg.properties.contributionType
    appId: MetaOapg.properties.appId
    contributionData: MetaOapg.properties.contributionData
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributionType"]) -> MetaOapg.properties.contributionType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributionData"]) -> MetaOapg.properties.contributionData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contributionGroup"]) -> MetaOapg.properties.contributionGroup: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["appId", "contributionType", "contributionData", "contributionGroup", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appId"]) -> MetaOapg.properties.appId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributionType"]) -> MetaOapg.properties.contributionType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributionData"]) -> MetaOapg.properties.contributionData: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contributionGroup"]) -> typing.Union[MetaOapg.properties.contributionGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["appId", "contributionType", "contributionData", "contributionGroup", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        contributionType: typing.Union[MetaOapg.properties.contributionType, str, ],
        appId: typing.Union[MetaOapg.properties.appId, str, ],
        contributionData: typing.Union[MetaOapg.properties.contributionData, dict, frozendict.frozendict, ],
        contributionGroup: typing.Union[MetaOapg.properties.contributionGroup, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContributionRequest':
        return super().__new__(
            cls,
            *args,
            contributionType=contributionType,
            appId=appId,
            contributionData=contributionData,
            contributionGroup=contributionGroup,
            _configuration=_configuration,
            **kwargs,
        )
