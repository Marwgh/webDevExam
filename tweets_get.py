from bottle import view , get 

@get("/tweets")
@view("tweets")

def _():
        
    return 