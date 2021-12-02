''' main file '''
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import router

''' main app '''
app = FastAPI()

''' cors '''
origins = [
    'http://localhost:3000',
    'https://anonymization-cli.herokuapp.com'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

''' include router '''
app.include_router(router.router)

''' root endpoint '''
@app.get('/')
async def root():
    print('Server Initiated')

''' run uvicorn server '''
if __name__=='__main__':
    uvicorn.run('main:app',host='localhost',
        port=4557, reload=True, debug=True, workers=3)