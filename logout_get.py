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
        encoded_jwt = request.get_cookie("jwt")
        user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 
        print(user_info)
        print(g.SESSIONS)

        response.status = 200
        return  dict(user_email=user_info["user_email"], user_id=user_id)
        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}