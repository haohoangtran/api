from flask import Flask
import mlab
from flask_restful import Api
from resources.user_resource import *
from resources.checkin_resource import *
from resources.schdule_resource import SchduleRes


mlab.connect()

app = Flask(__name__)

api = Api(app)
api.add_resource(UserRegister,"/register")
api.add_resource(UserLogin,"/login")
api.add_resource(Checkin,"/checkin")
api.add_resource(SchduleRes,"/schdule")
@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    return response

if __name__ == '__main__':
    app.run()
