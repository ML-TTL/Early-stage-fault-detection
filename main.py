from fastapi import FastAPI,UploadFile,File
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import shutil

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World~~"}
    
# from fastapi import FastAPI
# import tensorflow as tf
# from pydantic import BaseModel
# app = FastAPI()

@app.post("/file")
async def root(file:UploadFile=File(...)):
    with open(f'{file.filename}','wb') as buffer:
        shutil.copyfileobj(file.file,buffer)
    ten=make_prediction(file.filename)
    return {"fase":ten}

def make_prediction(file):
    df=pd.DataFrame(columns=[["PGV1","PGV2","PGV3","ATB1","ATB2"]])
    model=load_model('model_l20_e10_ns_np.h5')
#    data = np.array(data).reshape(1, -1)
    data= pd.read_csv(file,usecols =["PGV1","PGV2","PGV3","ATB1","ATB2"])
    #pred=model.predict(data)
    #prediction = model.predict(data)
    mean=pd.read_csv("mean.csv",usecols =["0"])
    
    m=np.array(mean)
    m=m.reshape(1,-1)


    std=pd.read_csv("std.csv",usecols =["0"])
    s=np.array(std)
    s=s.reshape(1,-1)
    df=pd.DataFrame(data)
    
    num=np.array(df)
    num_norm=(num - m)/(s)
    dict1={}
    for i in range(len(num_norm)//20):
        if len(num_norm)-(20*(i+1))<20:
            break
        temp_norm=num_norm[20*(i):20*(i+1)]
        t=model.predict(tf.expand_dims(temp_norm, axis=0))
        pred=np.argmax(t, axis=1)
        p=int(pred+1)
        name="section "+str(i+1)
        dict1[name]=p

        


    #pred=model.predict(df)
    #m=np.array(df)
    #prediction = model.predict(data)
    #return dict(enumerate(m.flatten(), 1))
    #return df.head()
    #return df.to_dict(orient="records")#(df.to_numpy()).item()
    return dict1
    
# @app.post("/predict")
# def predict(data: List[float]):
#     prediction = make_prediction(data)
#     return {"prediction": prediction}
