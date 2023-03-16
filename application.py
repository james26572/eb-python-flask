import flask
import os
from test import add10
 
application = flask.Flask(__name__)

# Only enable Flask debugging if an env var is set to true
application.debug = os.environ.get('FLASK_DEBUG') in ['true', 'True']

# Get application version from env
app_version = os.environ.get('APP_VERSION')

# Get cool new feature flag from env
enable_cool_new_feature = os.environ.get('ENABLE_COOL_NEW_FEATURE') in ['true', 'True']

@application.route('/',methods = ["POST","GET"])
def home():
    
    if flask.request.method == "POST":
        number = flask.request.form['ticker']
        return str(add10(int(number)))
    else:
        return flask.render_template('index.html',
                                    
                                    flask_debug=application.debug,
                                    app_version=app_version,
                                    enable_cool_new_feature=enable_cool_new_feature,
                                    )
 
if __name__ == '__main__':
    application.run(host='0.0.0.0')
