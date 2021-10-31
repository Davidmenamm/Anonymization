""" Program Main File """
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from endpoints import router


""" main app """
app = FastAPI()

""" cors """
origins = [
    'http://localhost:3000',
    'https://anonymization-cli.herokuapp.com'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router)

""" root endpoint """
@app.get("/")
async def root():
    path = 'data/hypothesis_0.csv'
    # dataset
    dataset = pd.read_csv(path, engine='c')
    # target
    target = dataset.iloc[:, 0]
    # features
    features = dataset.iloc[:, 1: len(dataset.columns)-1]


""" uvicorn server run """
if __name__=="__main__":
    uvicorn.run("main:app",host='localhost', port=4557, reload=True, debug=True, workers=3)