from flask import Flask 
from dotenv import load_dotenv
import os
from api.auth.controller import auth_api
from api.user.controller import user_api
from config.db import config_db


if __name__ == "__main__":

  load_dotenv()
  app = Flask(__name__)
  config_db(app)
  app.register_blueprint(auth_api, url_prefix='/auth')
  app.register_blueprint(user_api, url_prefix='/user')
  app.run(
    port = int(os.getenv("PORT")), 
    host = os.getenv("HOST"),
    debug=True
  )
