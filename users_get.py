from bottle import view , get 

@get("/users")
@view("users")

def _():
        
    return 