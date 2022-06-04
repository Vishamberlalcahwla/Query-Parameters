from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/myname/{name}")
def mynameis(name:str,lastname: Union[str, None] = None):
    if lastname:
        return {"name" : name , "lastname" :lastname}
    return {"name" : name }     

