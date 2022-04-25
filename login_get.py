from bottle import view , get ,request , response
import jwt
import g
@get("/login")
@view("login")

def _():
    try:
        if not request.params.get("error"):
            error= ""
        else:
            response.status = 400
            error = request.params.get("error")

        if not request.params.get("user_email"):
            user_email =""
        else:
            response.status = 400
            user_email = request.params.get("user_email")
        
        if request.get_cookie("jwt") :
            encoded_jwt = request.get_cookie("jwt")
            user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 
            if user_info == "" :
                user_id = ""
            else :
                user_id = user_info["user_id"]
        else :
            user_id =""
        response.status = 200
        return  dict(error=error , user_email=user_email , user_id=user_id)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}