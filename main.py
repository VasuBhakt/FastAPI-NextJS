from fastapi import Depends, FastAPI, HTTPException, Query
from models import Product, ProductUpdate;
from database import engine, session
import db_models
from sqlalchemy.orm import Session;

app = FastAPI();

def get_db() :
    db = session()
    try :
        yield db;
    finally :
        db.close()

db_models.Base.metadata.create_all(bind=engine)

@app.get('/')
def greet(
    name: str = Query(),
    count : int = Query()
) :
    while(count>0) :
        print('Hello,', name);
        count-=1;

@app.get('/products')
def get_all_products(db : Session = Depends(get_db)) : 
    db_products = db.query(db_models.Product).all();
    if db_products is None :
        raise HTTPException(status_code=404, detail="No products")
    return db_products;

@app.get('/products/{id}')
def get_product_by_id(id: int, db : Session = Depends(get_db)) :
    product = db.query(db_models.Product).filter(db_models.Product.id == id).first();
    if product is None :
        raise HTTPException(status_code=404, detail="Product not found")
    return product;

@app.post('/product/create')
def create_product(product: Product, db : Session = Depends(get_db)) :
    db.add(db_models.Product(**product.model_dump()))
    db.commit()
    return "Product added successfully!"

@app.put('/products/{id}')
def update_product(id: int, product: ProductUpdate, db : Session = Depends(get_db)) :
    db_product = db.query(db_models.Product).filter_by(id=id).first();
    if db_product is None :
        raise HTTPException(status_code=404, detail="Product not found")
    data = product.model_dump(exclude_unset=True)
    for key, value in data.items() :
        setattr(db_product, key, value)
    db.commit();
    return "Product updated successfully!";

@app.delete('/products/{id}')
def delete_product(id: int, db: Session = Depends(get_db)) :
    db_product = db.query(db_models.Product).filter_by(id=id).first();
    if db_product is None :
        raise HTTPException(status_code=404, detail="Product not found")
    db.query(db_models.Product).filter_by(id=id).delete();
    db.commit();
    return "product deleted successfully"