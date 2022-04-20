from cmath import pi
from bottle import post , request , redirect , response
import g
import uuid
import time
import jwt
import os






@post("/create")
def _():
    print("#"*60)
    if not request.forms.get("tweet_description") :
      response.status = 400
      return redirect("/tweet")
    
    if len(g.SESSIONS) < 1 :
      response.status = 400
      redirect("/login?error=invalidS")
    if not (request.get_cookie("jwt")) :
      response.status = 400
      redirect("/login?error=invalidS")

    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256") 

    
    try:
      if request.files.get("tweet_image") :
        image = request.files.get("tweet_image")
        description = request.forms.get("tweet_description")
        id = str(uuid.uuid4())
        issue_time = time.ctime( int(time.time()) )
        image_name = image.filename.strip().replace(" ", "-")
        
        #save image if not in the image folder
        

        if image_name in os.listdir("./image"):
          print("i am in ")
        else :
          print("i am not in")
          image.save(f"image/{image_name}")
        # for file in os.listdir("./image"):
        #   file_name = os.fsencode(file)
        #   if image_name == file_name :  
        #     print(image_name)
        #   else :
        #     print("yes i want it")
        


        tweet={ "description" : description , "id": id , "iat" : issue_time  , "image": image_name , "user_id" :user_info["user_id"]}
        g.TWEETS.append(tweet)

        is_image = "true"
        response.status = 200
        return id , is_image  , issue_time 


      is_image = "fals"
    
      description = request.forms.get("tweet_description")
      id = str(uuid.uuid4())
      issue_time = time.ctime( int(time.time()) )

      tweet={ "description" : description , "id": id , "iat" : issue_time ,"image": ""  , "user_id" :user_info["user_id"]}
      g.TWEETS.append(tweet)

      response.status = 200
      return id  , is_image , issue_time


    except Exception as ex:
      print(ex)
      print("#"*60)
      response.status = 500
      return {"info":"upsss.... something went wrong"}
    