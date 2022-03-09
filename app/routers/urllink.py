from pydantic import BaseModel
from typing import Optional


class URLLink(BaseModel):
    url: Optional[str] = None
