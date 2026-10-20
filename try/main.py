from fastapi import FastAPI, Request
from dtos import ProductDTO

app = FastAPI()



global products
from mockdata import products


@app.get("/")
def home():
    return "Welcome to Home"


@app.get("/products")
def get_products():
    return products


# Path parameter
@app.get("/product/{product_id}")
def get_particular_product(product_id:int):

    for i in products:
        if i['id'] == product_id:
            return i

    return {"Error":f"Product Not found for this ID: {product_id}"}


# :::::::::::::::::::: Query parameter ::::::::::::::::::::


# For Fixed parameter
# @app.get("/greet/name={name}&age={age}")
# def greet(name:str,age:int):
#     return {"message":f"Hello {name}, How are You! Your age is {age}"}



# For non Fixed parameter like n
@app.get("/greet")
def greet_user(request:Request):
    print(">>>>>>>>>>",request)
    print(request.query_params)
    query_params = dict(request.query_params)
    print("<<",query_params)
    name = query_params['name']
    age = query_params['age']

    return {"Name":name, "Age":age}






@app.post("/create_product")
def create_porduct(product_data:ProductDTO):

    product_data = product_data.model_dump()
    products.append(product_data)
    
    return {"message":"Product created Successfully...","Data":products}



@app.put("/update_product/{product_id}")
def update_porduct(product_data:ProductDTO, product_id:int):

    product_data = product_data.model_dump()
    ret_data = {}
    
    name = product_data.get("name","")
    price = product_data.get("price","")
    count = product_data.get("count","")
    
    for index, onedata in enumerate(products):
        if onedata['id'] == product_id:

            print("Data Found !!!")
            onedata['name'] = name
            onedata['price'] = price
            onedata['count'] = count

            ret_data = onedata

    print(f"one Data : {onedata}")

    if ret_data:
        return {"message":"Product Updated Successfully...","Data":ret_data}

    return {"error":"Unable to Find the product..."}


@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):

    for index, onedata in enumerate(products):
        if onedata['id'] == product_id:
            deleted_product = products.pop(index)
            return {"message":"Product Deleted Successfully...","Data":deleted_product}


    return {"message":"Product Not Found...","Data":products}

