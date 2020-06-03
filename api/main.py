from fastapi import FastAPI
from whereamigeo.helper import olc_to_phrase, phrase_to_olc

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "up"}


@app.get("/lookup_olc")
def read_item(olc: str = None):
    olc = olc.replace(' ', '+')
    return {"phrase": olc_to_phrase(olc, False)}


@app.get("/lookup_phrase")
def read_item(phrase: str = None):
    return {"olc": phrase_to_olc(phrase)}
