from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user/register")
def user_registration_process():
    # prepare setup to take the following pramameters
    # - firstname
    # - lastname
    # - mobile_number
    # - email
    # - date of birth

    # verify details and write into a csv file

    # create a table in postgres

    # push the data into postgres if all is ok

    return True