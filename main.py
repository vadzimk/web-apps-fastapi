import fastapi.responses
from fastapi import FastAPI
from fastapi_chameleon import template, global_init
import uvicorn

global_init('templates')
app = FastAPI()


@app.get('/')
@template(template_file='index.html')
def index(user: str = 'anon'):

    return {
        'user_name': user
    }

if __name__ == '__main__':
    uvicorn.run  (app)