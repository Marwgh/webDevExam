from bottle import view , get 

@get("/logout")
@view("logout")

def _():
        
    return 