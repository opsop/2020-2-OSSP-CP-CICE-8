from flask import Flask
#import blueprint

from flask_restplus import Api
from flask import Blueprint

from msg_app.emergency_alerts_controller import api as emergency_alerts_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CICE Open API',
          version='1.0',
          description='CICE Open API'
          )

api.add_namespace(emergency_alerts_ns, path='/emergency_alerts')

app = Flask(__name__)

app.register_blueprint(blueprint)


app.run(host='0.0.0.0')