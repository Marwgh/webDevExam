from bottle import  default_app , get , view , run , static_file , response , request
import g
import jwt



#################################################################
import tweet_delete                                        #DELETE

import tweet_post                                          #POST
import signup_post                                         #POST
import login_post                                          #POST
import logout_post                                         #POST

import tweet_put                                           #PUT
import verify_put                                          #PUT

import admin_get                                           #GET
import signup_get                                          #GET
import logout_get                                          #GET
import login_get                                           #GET
import users_get                                           #GET
import tweets_get                                          #GET
#################################################################

@get("/")
@view("index")
def _():
  if request.get_cookie("jwt") :
    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 
    if user_info == "" :
      user_id = ""
    else :
      user_id = user_info["user_id"]
  else :
    user_id=""

  return dict(tweets = g.TWEETS , user_id = user_id)
#################################################################

@get("/validator.js")
def _():
  return static_file("validator.js", root=".")
#################################################################

@get("/app.css")
def _():
  return static_file("app.css", root=".")
#################################################################
@get("/app.js")
def _():
  return static_file("app.js", root=".")


#################################################################
@get("/image/<image_name>")
def _(image_name):
  return static_file(image_name, root="./image")

#################################################################
@get("/svg/<svg_name>")
def _(svg_name):
  return static_file(svg_name, root="./svg")


try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=4443, debug=True, reloader=True, server="paste")
