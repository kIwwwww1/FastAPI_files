import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI()

@app.post('/files')
async def upload_file(upload_file: UploadFile):
    file = upload_file.file
    filename = upload_file.filename
    with open(f'1_{filename}', 'wb') as f:
        f.write(file.read())


@app.post('/multiple-files')
async def upload_files(upload_files: list[UploadFile]):
    for index, upload_file in enumerate(upload_files):
        file = upload_file.file
        filename = upload_file.filename
        with open(f'{index}_{filename}', 'wb') as f:
            f.write(file.read())

@app.get('/files/{filename}')
async def get_file(filename: str):
    return FileResponse(filename)


def iterfile(filename):
    with open(filename, 'rb') as file:
        while chunk := file.read(1024 * 1024):
            yield chunk


@app.get('/files/streaming/{filename}')
async def get_streamig_file(filename: str):
    return StreamingResponse(iterfile(filename), media_type='video/mp4')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
