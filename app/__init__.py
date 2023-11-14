import os.path
from pathlib import Path

from flask import Flask

app = Flask(__name__)

@app.get("/")
def read_root():
    return {"xf api"}

@app.get("/items/<locale>/<fid>")
def read_item(locale: str, fid: str):
    fullpath = os.path.join(Path(__file__).parent, f"data/{locale}/{fid[0:2]}/{(fid)[2:]}.txt")
    xftext = "N/A"
    with open(fullpath, "r", encoding="utf-8") as ffile:
       xftext = ffile.readlines()[0]
    return {"version": "pilot", "factid": fid, "locale": locale, "xfact": xftext}