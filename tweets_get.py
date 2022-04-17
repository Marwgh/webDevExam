from bottle import view , get , request , redirect , response
import jwt
import g

@get("/tweets")
@view("tweets")

def _():
    if len(g.SESSIONS) < 1 :
        redirect("/login?error=invalidS")
    if not (request.get_cookie("jwt")) :
        redirect("/login?error=invalidS")

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 

    for session in g.SESSIONS :
        if not session['user_id'] == user_info["user_id"]:
            redirect("/login?error=invalidS")
    try:
        return dict(tweets=g.TWEETS, user_id = user_info["user_id"] )

    
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}