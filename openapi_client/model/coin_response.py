# coding: utf-8

"""
    Hugs Platform - OpenAPI 3.0

    The Hugs Platform API  # noqa: E501

    The version of the OpenAPI document: 1.0.1
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


class CoinResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            coin_id = schemas.StrSchema
            name = schemas.StrSchema
            abbreviature = schemas.StrSchema
            image = schemas.StrSchema
            last_updated = schemas.StrSchema
            price = schemas.NumberSchema
            market_cup = schemas.NumberSchema
            click = schemas.IntSchema
            __annotations__ = {
                "coin_id": coin_id,
                "name": name,
                "abbreviature": abbreviature,
                "image": image,
                "last_updated": last_updated,
                "price": price,
                "market_cup": market_cup,
                "click": click,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_id"]) -> MetaOapg.properties.coin_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["abbreviature"]) -> MetaOapg.properties.abbreviature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_updated"]) -> MetaOapg.properties.last_updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["market_cup"]) -> MetaOapg.properties.market_cup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["click"]) -> MetaOapg.properties.click: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["coin_id", "name", "abbreviature", "image", "last_updated", "price", "market_cup", "click", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_id"]) -> typing.Union[MetaOapg.properties.coin_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["abbreviature"]) -> typing.Union[MetaOapg.properties.abbreviature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_updated"]) -> typing.Union[MetaOapg.properties.last_updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["market_cup"]) -> typing.Union[MetaOapg.properties.market_cup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["click"]) -> typing.Union[MetaOapg.properties.click, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["coin_id", "name", "abbreviature", "image", "last_updated", "price", "market_cup", "click", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        coin_id: typing.Union[MetaOapg.properties.coin_id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        abbreviature: typing.Union[MetaOapg.properties.abbreviature, str, schemas.Unset] = schemas.unset,
        image: typing.Union[MetaOapg.properties.image, str, schemas.Unset] = schemas.unset,
        last_updated: typing.Union[MetaOapg.properties.last_updated, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        market_cup: typing.Union[MetaOapg.properties.market_cup, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        click: typing.Union[MetaOapg.properties.click, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CoinResponse':
        return super().__new__(
            cls,
            *_args,
            coin_id=coin_id,
            name=name,
            abbreviature=abbreviature,
            image=image,
            last_updated=last_updated,
            price=price,
            market_cup=market_cup,
            click=click,
            _configuration=_configuration,
            **kwargs,
        )
