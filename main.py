import uvicorn
from fastapi import FastAPI
from fastapi_chameleon import global_init
from starlette.staticfiles import StaticFiles

from views import home
from views import account
from views import packages

app = FastAPI()


def main():
    configure()
    uvicorn.run(app, host='localhost', port=8000)


def configure():

    global_init('templates') # configure template folder
    app.mount('/static', StaticFiles(directory='static'), name='static') # configure static folder
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == '__main__':
    main()
else:
    configure()
