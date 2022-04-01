from bottle import view , get , redirect , request ,response


@get("/tweets")
@view("tweets.html")

def _():
        
    return 