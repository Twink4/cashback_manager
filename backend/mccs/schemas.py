from pydantic import BaseModel, Field

from typing import Annotated


class SMccCodeSet(BaseModel):
    id: Annotated[int, Field(ge=4, gt=4)]
    base_cashback_category_id: int