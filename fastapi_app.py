from fastapi import FastAPI, File, UploadFile  #python 3.6+
from typing_extensions import Annotated  #python 3.6+
#from typing import Annotated #python 3.9+
#from fastapi import FastAPI, File, UploadFile #python 3.9+
from pypdf import PdfReader
import json

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    new_file = open('bar.txt', 'rw')
    shutil.copyfileobj(file, new_file)
    file.close()
    return {"filename": file.filename}

@app.post("/predict")
async def create_file(file: bytes = File(...)):
    with open("TempFile.pdf", 'wb') as f:
        f.write(file)
    reader = PdfReader("TempFile.pdf")
    EmulateListResult=[[1,"sfsfs",97],[1,"sfsfs",97],[1,"sfsfs",97]]
    return {"result":json.dumps(EmulateListResult)}
