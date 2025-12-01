import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/files')
async def upload_file(upload_file: UploadFile):
    file = upload_file.file
    filename = upload_file.filename
    with open(f'1_{filename}', 'wb') as f:
        f.write(file.read())


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)