from fastapi import FastAPI
app = FastAPI()
alnafi_st_db = [
    {"st_name": "ALi"}, {"st_name": "Aslam"}, 
    {"st_name": "Vishamber"},
    {"st_name": "Fasil Sir"},
    {"st_name": "Ali"}
]
@app.get("/get_st_data")
def get_st_data(frm: int,to:int):
    return alnafi_st_db[frm:frm+to]

