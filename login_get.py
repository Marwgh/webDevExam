from bottle import view , get ,request , response
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
        
        response.status = 200
        return  dict(error=error , user_email=user_email , sessions = g.SESSIONS)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}