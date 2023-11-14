import os.path
from pathlib import Path

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{locale}/{fid}")
def read_item(locale: str, fid: str):
    fullpath = os.path.join(Path(__file__).parent, f"data/{locale}/{fid[0:2]}/{(fid)[3:]}.txt")
    xftext = "N/A"
    with open(fullpath, "r") as ffile:
       xftext = ffile.readlines();
    return {"version": "pilot", "factid": fid, "locale": locale, "xfact": xftext}