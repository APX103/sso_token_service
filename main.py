import yaml
import uvicorn
from fastapi import FastAPI

import openxlab

app = FastAPI()

with open("config.yaml", ) as f:
    config = yaml.load(f.read(), yaml.FullLoader)

@app.get("/")
def root():
    token = openxlab.xlab.handler.user_token.get_jwt(config["ak"], config["sk"])
    return {"token": token}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10086)
