from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class Product(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    name: str
    price: float
    description: Optional[str] = None
    stock: int

    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)


class ProductDBModel(Product):
    def model_dump(
        self,
        *,
        mode="python",
        include=None,
        exclude=None,
        context=None,
        by_alias=None,
        exclude_unset=False,
        exclude_defaults=False,
        exclude_none=False,
        round_trip=False,
        warnings=True,
        fallback=None,
        serialize_as_any=False,
    ):
        data = super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
            fallback=fallback,
            serialize_as_any=serialize_as_any,
        )
        if "_id" in data and isinstance(data["_id"], ObjectId):
            data["_id"] = str(data["_id"])
        return data
