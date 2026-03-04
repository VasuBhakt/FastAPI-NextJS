from typing import Optional
from pydantic import BaseModel 

class Product(BaseModel) :
    id : int
    name: str
    description : str
    price : float
    quantity : int

class ProductUpdate(BaseModel) :
    name : Optional[str] = None 
    description : Optional[str] = None
    price : Optional[float] = None
    quantity : Optional[int] = None


    # def __init__(self, id: int, name: str, description: str, price: float, quantity: int ) :
    #     self.id = id;
    #     self.name = name;
    #     self.description = description;
    #     self.price = price;
    #     self.quantity = quantity;