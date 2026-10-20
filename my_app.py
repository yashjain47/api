from re import X
import uvicorn
from fastapi import FastAPI,Path, Request
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')



app = FastAPI(title="First Application")


class Student(BaseModel):
    id:int
    name:str = Field(title="Name of the Student",max_length=10)
    subjects:List[str] = []



@app.get("/")
async def index() -> dict:
    return {"message":"Home Page"}


'''
Path Parameter like in URL(endpoints)
like name and age here is path parameter
'''
@app.get("/user/{name}/{age}")
async def user_details(name:str,age:int) -> dict:
    return {"message":f"Name :{name}, Age: {age}"}


'''like
Query Parameter --> http://127.0.0.1:7000/hello?name=Ravi&age=20&marks=90 
like name ,age and marks here is query parameter
'''
# @app.get("/hello")
# async def hello(*, name: str=Path(...,min_length=3 , max_length=10), age: int = Path(..., ge=1, le=100),marks:int = Path(..., ge=1, le=100)):
#     return {"message":f"Name :{name}, Age: {age}, Marks:{marks}"}



@app.post("student")
async def student_data(s1:Student):
    return s1



@app.get("/hello")
async def hello(request: Request):
    
    ret='''
        <html>
        <body>
        <h2>Hello World!</h2>
        </body>
        </html>
        '''

    return HTMLResponse(content=ret,status_code=200)


@app.get("/hello/{name}",response_class=HTMLResponse)
async def hello1(request: Request,name:str):
    return templates.TemplateResponse("index.html",{"request":request,"name":name})



if __name__ == "__main__":
    uvicorn.run("my_app:app",host="127.0.0.1",port=7000,reload=True)
