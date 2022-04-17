from bottle import view , get ,request , response

@get("/login")
@view("login")

def _():
    try:
        if not request.params.get("error"):
            error= ""
        else:
            error = request.params.get("error")

        if not request.params.get("user_email"):
            user_email =""
        else:  
            user_email = request.params.get("user_email")

        return  dict(error=error , user_email=user_email)

    except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}