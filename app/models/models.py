from pydantic import BaseModel
from typing import Optional

class ArticleModel(BaseModel):
    url: str
    html: Optional[str] = None
