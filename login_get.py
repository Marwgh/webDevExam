from distutils.log import error
from bottle import view , get 

@get("/login")
@view("login")

def _():
        
    return dict(error="")