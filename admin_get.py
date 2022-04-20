from bottle import get, view
import g

@get("/adminPanel")
@view("admin")
def _():
  return dict(tweets = g.TWEETS )