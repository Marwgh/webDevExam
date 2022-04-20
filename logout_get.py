from bottle import view , get , request, redirect , response
import jwt
import g


@get("/logout")
@view("logout")

def _():
    if len(g.SESSIONS) < 1 :
        response.status =400
        return redirect("/login?error=invalidS")
    if not (request.get_cookie("jwt")) :
        response.status =400
        return redirect("/login?error=invalidS")

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 

    for  session in g.SESSIONS :
        if not session['user_id'] == user_info["user_id"]:
            response.status =400
            return redirect("/login?error=invalidS")
    try: 
        
        encoded_jwt = request.get_cookie("jwt")
        user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 
        print(user_info)
        print(g.SESSIONS)

        response.status = 200
        return  dict(user_email=user_info["user_email"], sessions = g.SESSIONS)
        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}