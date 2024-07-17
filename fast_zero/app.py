from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Jesus Cristo meu Salvador'}


@app.get('/livro', response_class=HTMLResponse)
def read_livro():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
