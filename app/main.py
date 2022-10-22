from fastapi import FastAPI, UploadFile

from app.predict import make_prediction


app = FastAPI(redoc_url=None)


@app.post("/predict", status_code=201)
async def predict(file: UploadFile):
    return make_prediction(file.file)
