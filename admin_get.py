from bottle import get, view, response,redirect, request
import g
import jwt

@get("/adminPanel")
@view("admin")
def _():
  if len(g.SESSIONS) < 1 :
    response.status = 400
    return redirect("/login?error=invalidS")
  if not (request.get_cookie("jwt")) :
    response.status = 400
    return redirect("/login?error=invalidS")
  encoded_jwt = request.get_cookie("jwt")
  user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256")

  if not (user_info["user_id"] == "admin1"):
    return redirect("/login?error=invalidS")



  return dict(tweets = g.TWEETS )