from bottle import  default_app , get , view , run , static_file


##############################

@get("/")
@view("index")
def _():
  return 
##############################
@get("/validator.js")
def _():
  return static_file("validator.js", root=".")

##############################
@get("/app.css")
def _():
  return static_file("app.css", root=".")
##############################



try:
  import production
  application = default_app()
except Exception as ex:
  print("Server running on development")
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
