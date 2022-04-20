from bottle import view , get 
import g

@get("/signup")
@view("signup")

def _():
        
    return dict( sessions = g.SESSIONS)