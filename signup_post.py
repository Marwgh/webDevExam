from bottle import post, redirect , request , response
import uuid
import g


@post("/signup")
def _():
  if not request.forms.get("user_name"):
    response.status = 400
    return redirect("/signup")
  if not request.forms.get("user_email"):
    response.status = 400
    return redirect("/signup")
  user_email = request.forms.get("user_email")
  
  for user in g.USERS :
    if request.forms.get("user_email") == user["email"]:
      response.status = 400
      return redirect("/signup")


  if not request.forms.get("user_password"):
    response.status = 400
    return redirect("/signup")
  if len(request.forms.get("user_password")) < 6 :
    response.status = 400
    return redirect("/signup")
  if len(request.forms.get("user_password")) > 20 :
    response.status = 400
    return redirect("/signup")

  
  try:
    print("yes im am sing in")
    user_name = request.forms.get("user_name")
    user_password = request.forms.get("user_password")
    user_id = str(uuid.uuid4())
    user = { "id": user_id , "email":user_email , "name":user_name , "password":user_password , "fake" : "false"}
    g.USERS.append(user)
    print(g.USERS)
    
    
    response.status=200
    return "valide"

  except Exception as ex:
        print(ex)
        response.status = 500
        return {"info":"upsss.... something went wrong"}
  