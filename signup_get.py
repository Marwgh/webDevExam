from bottle import view , get , request
import jwt
import g

@get("/signup")
@view("signup")

def _():
        
    if request.get_cookie("jwt") :
        encoded_jwt = request.get_cookie("jwt")
        user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 
        if user_info == "" :
            user_id = ""
        else :
            user_id = user_info["user_id"]
    else:
        user_id =""

    return dict( user_id=user_id)