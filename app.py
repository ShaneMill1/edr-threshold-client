from flask import jsonify,Flask,render_template, send_from_directory, send_file, request
from flask_cors import *
app = Flask(__name__, static_url_path='/static',static_folder='static')


CORS(app)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__": 
   app.run(host='0.0.0.0',port=5300)

