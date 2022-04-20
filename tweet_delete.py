from bottle import  delete , redirect , response
import g


@delete("/delete/<tweet_id>")
def _(tweet_id):
  #VALIDATION 


  if not tweet_id :
    response.status = 400
    return redirect("/tweet")
  
  try:
    print("#"*30)
    print(tweet_id)
    print("#"*30)
    for  index ,tweet in enumerate(g.TWEETS):
      if tweet["id"] == tweet_id:
          response.status = 200
          g.TWEETS.pop(index)
          
  except Exception as ex:
    print(ex)
    response.status = 500
    return {"info":"upsss.... something went wrong"}




