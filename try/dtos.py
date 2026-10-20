from pydantic import BaseModel


class ProductDTO(BaseModel):

    id: int
    name: str
    price: int = 0
    count: int = 0