from fastapi import Body, FastAPI, Query
from fastapi.params import Param
from models import Product;

app = FastAPI();

@app.get('/')
def greet(
    name: str = Query(),
    count : int = Query()
) :
    while(count>0) :
        print('Hello,', name);
        count-=1;

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
    return [d for d in products if d.id==id][0];


@app.post('/product/create')
def createProduct(product: Product) :
    products.append(product);
    return products;



@app.put('/products/{id}')
def updateProduct(id: int, product: Product) :
    for i in range(len(products)) :
        if products[i].id == id :
            products[i] = product;
            return products;
    return products; 

@app.delete('/products/{id}')
def deleteProduct(id: int) :
    for i in range(len(products)) :
        if products[i].id==id :
            del products[i];
            return products;
    return products;