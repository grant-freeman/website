from flask import *
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username': 'Grant'}
    return render_template('index.html', title='Home', user=user)
