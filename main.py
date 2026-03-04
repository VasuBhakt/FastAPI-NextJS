from fastapi import Body, FastAPI
from fastapi.params import Param
from models import Product;

app = FastAPI();

@app.get('/')
def greet() :
    return "Hello world!"

products = [
    Product(id=1, name="phone", description="budget phone", price=8000, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=56000, quantity=4),
    Product(id=3, name="pen", description="blue ink pen", price=5, quantity=100),
    Product(id=4, name="table", description="wooden table", price=5000, quantity=20),

]

@app.get('/products')
def getAllProducts() : 
    return products;

@app.get('/products/{id}')
def getProductById(id: int) :
    return products[id-1];

@app.post('/product/create')
def createProduct(product: Product) :
    products.append(product);
    return products;

