from bottle import post , request  , response
import jwt
import g

@post("/logingout") 
def _():
  try:
    if not request.get_cookie("jwt") :
      return "/login?error=invalidS"

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 
    session = user_info
    g.SESSIONS.remove(session)
    
    return "/"
  except Exception as ex:
      print(ex)
      response.status = 500
      return {"info":"upsss.... something went wrong"}