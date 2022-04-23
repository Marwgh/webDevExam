from bottle import post , request , response
import g 
import re
import time
import jwt
import uuid


@post("/login")
def _():
  try:
      if not request.forms.get("user_email"):
        response.status = 400
        return "/login?error=user_email"
      if not re.match( g.REGEX_EMAIL , request.forms.get("user_email")):
        response.status = 400
        return "/login?error=user_email"

      user_email = request.forms.get("user_email")

      if not request.forms.get("user_password"):
        response.status = 400
        return f"/login?error=user_password&user_email={user_email} "
      if not (request.get_cookie("jwt")) :
        g.SESSIONS = []
        
        
      if len(g.SESSIONS) > 0 :
        return "/logout"
      user_password = request.forms.get("user_password")
      print("**************yes")
      print("**************")
      print(g.USERS)
      if user_password == "adminPassword" and user_email == "admin@admin.com":
          ###############   MAKING THE SESSION AND COOKIE FOR ADMIN  #################
          user_session_id = str(uuid.uuid4())
          session = {"user_session_id" : user_session_id,"user_id":"admin1", "user_email" : "admin@admin.com", "iat" : int(time.time())}
          g.SESSIONS.append(session)
          print("#"*30)
          print(g.SESSIONS)
          encoded_jwt = jwt.encode(session, "theKey" , algorithm="HS256")
          response.set_cookie("jwt", encoded_jwt)

          response.status = 200
          return "/"
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
          response.status = 200
          return "/"

        
        
      response.status = 400
      return f"/login?error=user_password&user_email={user_email}"

  except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}
