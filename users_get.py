from bottle import view , get ,response , request ,redirect
import jwt
import g

@get("/users")
@view("users")

def _():
    if len(g.SESSIONS) < 1 :
        return redirect("/login?error=invalidS")
    if not (request.get_cookie("jwt")) :
        return redirect("/login?error=invalidS")

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 

    for  session in g.SESSIONS :
        if not session['user_id'] == user_info["user_id"]:
            return redirect("/login?error=invalidS")
    try:
        return dict(users=g.USERS , sessions=g.SESSIONS)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}