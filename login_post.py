from bottle import post , request , redirect, response
import g 
import re
import time
import jwt
import uuid


@post("/login")
def _():
    if not request.forms.get("user_email"):
      return "/login?error=user_email"
    if not re.match( g.REGEX_EMAIL , request.forms.get("user_email")):
      return "/login?error=user_email"

    user_email = request.forms.get("user_email")

    if not request.forms.get("user_password"):
      return f"/login?error=user_password&user_email={user_email}"


    user_password = request.forms.get("user_password")
    print("**************yes")
    print("**************")
    print(g.USERS)
    for user in g.USERS:
      if user["password"] == user_password and user["email"] == user_email:
        ###############   MAKING THE SESSION AND COOKIE  ##################
        user_session_id = str(uuid.uuid4())
        session = {"user_session_id" : user_session_id,"user_id":user["id"], "user_email" : user_email, "iat" : int(time.time())}
        g.SESSIONS.append(session)
        print("#"*30)
        print(g.SESSIONS)
        encoded_jwt = jwt.encode(session, "theKey" , algorithm="HS256")
        response.set_cookie("jwt", encoded_jwt)

        #SUCESS
        return "/"
    
    return f"/login?error=user_password&user_email={user_email}"
