from fastapi import APIRouter, FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.routers import Customer


# app = APIRouter()
app = FastAPI()

# Add a new customer
@app.post("/customer")
async def create_customer(item: Customer):

    # Encode the created customer item if successful into a JSON and return it to the client with 201
    json_compatible_item_data = jsonable_encoder(item)

    return JSONResponse(
        content=json_compatible_item_data,
        status_code=201
    )