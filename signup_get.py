from bottle import view , get 

@get("/signup")
@view("signup")

def _():
        
    return 