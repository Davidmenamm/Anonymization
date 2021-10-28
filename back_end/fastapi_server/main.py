""" Program Main File """
# imports
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

# main obj
app = FastAPI()

# cors
origins = [
    "http://localhost:3000",
    "http://localhost:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    # dataset
    dataset = pd.read_csv(r'back_end\\fastapi_server\\data\\hypothesis_0.csv', engine='c')
    # target
    target = dataset.iloc[:, 0]
    # features
    features = dataset.iloc[:, 1: len(dataset.columns)-1]
    # train / test
    X_train, X_test, y_train, y_test = train_test_split(
        features, target, stratify=target, train_size=0.67)
    # run classification
    nbc = GaussianNB()
    nbc.fit(X_train, y_train)
    y_pred = nbc.predict(X_test)
    acc = metrics.accuracy_score(y_test, y_pred)
    return {"accuracy": f"Accuracy is {acc}"}


if __name__=="__main__":
    uvicorn.run("main:app",host='localhost', port=4557, reload=True, debug=True, workers=3)