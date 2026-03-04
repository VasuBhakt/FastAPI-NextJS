from fastapi import FastAPI, params;

app = FastAPI()

@app.get('/')
def greet() :
    return "Hello !";