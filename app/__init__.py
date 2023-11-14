import os.path
from pathlib import Path

from flask import Flask

app = Flask(__name__)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/<locale>/<fid>")
def read_item(locale, fid):
    fullpath = os.path.join(Path(__file__).parent, f"data/{locale}/{fid[0:2]}/{(fid)[2:]}.txt")
    xftext = "N/A"
    with open(fullpath, "r", encoding="utf-8") as ffile:
       xftext = unicode(ffile.readlines()[0], 'utf-8');
    return {"version": "pilot", "factid": fid, "locale": locale, "xfact": xftext}