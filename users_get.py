from bottle import view , get ,response , request ,redirect
import jwt
import g

@get("/users")
@view("users")

def _():
    if len(g.SESSIONS) < 1 :
        response.status = 400
        return redirect("/login?error=invalidS")
    if not (request.get_cookie("jwt")) :
        response.status = 400
        return redirect("/login?error=invalidS")

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 

    for index, session in enumerate(g.SESSIONS) :
        if session['user_id'] == user_info["user_id"]:
            print("success")
        elif index == (len(g.SESSIONS)-1) :
            print(index)
            response.status = 400
            return redirect("/login?error=invalidS")
        print(index)
        

    try:
        if user_info == "" :
            user_id = ""
        else :
            user_id = user_info["user_id"]
        
        return dict(users=g.USERS , tweets = g.TWEETS , user_id =user_id)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}