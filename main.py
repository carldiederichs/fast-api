from urllib import response
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import requests
from PIL import Image
import io
import pandas as pd 
import matplotlib.pyplot as plt

app = FastAPI()

@app.get("/my-first-api")

def hello(name = None):
    if name is None:
        text = "hello"
    else: 
        text = 'Hello' + name + "!"
    return text

@app.get("/get-iris")
def get_iris():
    
    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    
    return iris

@app.get("/plot-iris")
def plot_iris():
    
    import pandas as pd     
    import matplotlib.pyplot as plt
    
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    
    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")
    
    return StreamingResponse(file, media_type="image/png")

# resp = requests.get('http://127.0.0.1:8000/plot-iris')
# file = io.BytesIO(resp.content)
# im = Image.open(file)
# im.show()

# resp = requests.get('http://127.0.0.1:8000/my-first-api?name=Ander')
# resp.text
     

