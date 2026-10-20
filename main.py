from fastapi import FastAPI, HTTPException
app = FastAPI()
from schemas import GenreURLChoices,Band


BANDS = [
    {'id':1,'name':'yash','roll':101},
    {'id':2,'name':'Tusher','roll':102},
    {'id':3,'name':'Rine','roll':103},
]

@app.get('/')
async def index() -> dict:
    return {'name':'yash'}

@app.get('/about')
async def about() -> str:
    return "Yash Jain"

@app.get('/bands')
async def bands() -> list[Band]:
    return [
        Band(**b) for b in BANDS
    ]

@app.get('/bands/{bands_id}')
async def band(bands_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == bands_id),None)
    if band is None:
        raise HTTPException(status_code=404,detail="Band Not Found")
    return band


