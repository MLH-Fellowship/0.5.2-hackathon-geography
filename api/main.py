from whereamigeo.helper import olc_to_phrase, phrase_to_olc
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "up"}


@app.get("/lookup_olc")
def lookup_olc(olc: str = None):
    # the '+' gets replaced with ' ' for some reason, we need to add it back
    olc = olc.replace(' ', '+')
    return {"phrase": olc_to_phrase(olc, False)}


@app.get("/lookup_phrase")
def lookup_phrase(phrase: str = None):
    return {"olc": phrase_to_olc(phrase)}
