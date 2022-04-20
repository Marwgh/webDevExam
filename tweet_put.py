from bottle import  put , request , response ,redirect
import g
import jwt

@put("/update")
def _():
  print("#"*40)
  print("# yes #")
  if not request.forms.get('tweet_text_updator'):
    response.status = 400
    return redirect("/tweet?error=invalidTweet")
  if not request.forms.get('tweet_id'):
    response.status = 400 
    return redirect("/tweet?error=invalidTweet")

  tweet_image_delete = "false"
  if request.forms.get('check_delete_image'):
    tweet_image_delete = request.forms.get('check_delete_image')
    print(tweet_image_delete )
    
  
  tweet_id = request.forms.get('tweet_id')
  updated_description = request.forms.get('tweet_text_updator').strip()


  
  print("#"*40)

  print(updated_description , tweet_id )
  if not ( updated_description ) :
    response.status = 400
    return redirect("/tweet?error=invalidTweet")

  
    
  try:
    encoded_jwt = request.get_cookie("jwt")
    user_info = jwt.decode(encoded_jwt ,  "theKey" , algorithms="HS256")  
    
    for tweet in g.TWEETS:
      if tweet["id"] == tweet_id:
          tweet["description"] = updated_description
          if not tweet_image_delete == "false" :
            tweet["image"] = ""
          print(tweet)
    
    response.status = 200
    return dict(user_id = user_info["user_id"] , tweets=g.TWEETS)



  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}