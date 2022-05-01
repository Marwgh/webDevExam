from bottle import  put , redirect , response
import g


@put("/verify/<user_id>")
def _(user_id):
  #VALIDATION 


  if not user_id :
    response.status = 400
    return redirect("/tweet")
  
  try:
    print("#"*30)
    print(user_id)
    print("#"*30)
    for user in g.USERS:
      if user["id"] == user_id:
          if user["fake"] == "false" :
            user["fake"] = "true"
            new_status = "you have been made a real fake"
          else :
            user["fake"] = "false"
            new_status = "you have been riped from you titel"


    for tweet in g.TWEETS:
      if tweet["user_id"] == user_id:
          if tweet["fake"] == "false" :
            tweet["fake"] = "true"
          else :
            tweet["fake"] = "false"
    
    response.status = 200
    return new_status

  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}



