from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from routers.customers import Customer
from routers.invoices import Invoice
from database.connector import select_customer, select_invoices


tmp_invoice_table = dict()

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


# Get a customer by customer id
@app.get("/customer/{customer_id}")
async def read_customer(customer_id: str):
    
    customer = select_customer(customer_id)

    # if customer id found in database
    if len(customer) == 1:
        id = customer.id.values[0]
        country = customer.country.values[0]
        
        item = Customer(customer_id=id, country=country)
        
        # Encode the customer into JSON and send it back
        json_compatible_item_data = jsonable_encoder(item)
        return JSONResponse(content=json_compatible_item_data)
    else:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="Item not found")


# Post a new invoice for a customer
@app.post('/customer/{customer_id}')
async def create_invoice(customer_id: str, invoice: Invoice):
    
    # Add the customer link to the invoice
    invoice.customer.url = "/customer/" + customer_id
    
    # Turn the invoice instance into a JSON string and store it
    jsonInvoice = jsonable_encoder(invoice)
    tmp_invoice_table[invoice.invoice_id] = jsonInvoice

    # Read it from the store and return the stored item
    ex_invoice = tmp_invoice_table[invoice.invoice_id]
    
    return JSONResponse(content=ex_invoice)


# Get a specific invoice by id
@app.get("/invoice/{invoice_id}")
async def read_invoice(invoice_id: int):
    
    # Read invoice from the dictionary
    ex_invoice = tmp_invoice_table[invoice_id]

    # Return the JSON that we stored
    return JSONResponse(content=ex_invoice)


# Return all invoices for a customer
@app.get("/customer/{customer_id}/invoice")
async def get_invoices(customer_id: str):
    
    ex_json = select_invoices(customer_id)

    # If customer is found in database
    if len(ex_json) > 0:
        return JSONResponse(content=ex_json)
    else:
        raise HTTPException(status_code=404, detail="No invoice for customer")