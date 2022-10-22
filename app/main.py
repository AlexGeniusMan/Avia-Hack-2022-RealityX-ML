from fastapi import FastAPI, UploadFile

from app.predict import make_prediction
from app.dependencies import get_settings


app = FastAPI(redoc_url=None, root_path=get_settings().root_path)


@app.post("/predict", status_code=201)
async def predict(file: UploadFile):
    return make_prediction(file.file)
