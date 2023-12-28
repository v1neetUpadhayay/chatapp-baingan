from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    firstname: str
    lastname: str
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/user/register")
def user_registration_process(item: Item):
    # prepare setup to take the following pramameters
    # - firstname
    # - lastname
    # - mobile_number
    # - email
    # - date of birth

    first_name = item.firstname
    # verify details and write into a csv file

    # create a table in postgres

    # push the data into postgres if all is ok
    if "all good":
        #save into postgres
        return True
    else:
        return "try again"