from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/myname/{firstname}/lastname/{lastname}")
def mynameis(firstname:str,lastname:str,caste: Union[str, None] = None):
    if caste:
        return {"firstname" : firstname , "lastname" :lastname, "caste":caste}
    return {"firstname" : firstname , "lastname" :lastname}   

