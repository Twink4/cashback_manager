from pydantic import BaseModel, Field

from typing import Annotated


class SMccCodeSet(BaseModel):
    mcc_code: Annotated[str, Field(min_length=4, max_length=4, pattern=r"^\d{4}$")]
    base_cashback_category_id: int
