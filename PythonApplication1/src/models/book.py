from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author: str
    year: int = Field(default=0)
    isbn: str = Field(..., pattern=r"^\d{10}|\d{3}-\d{10}$")



