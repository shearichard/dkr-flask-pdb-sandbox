from flask import Flask
from datetime import datetime

USE_PDB=True

app = Flask(__name__)

def a_function_to_step_into(n, m):
    output = n + m
    return output

    
@app.route("/hellopdb")
def hello_pdb():
    somedic = {"reason": 'only here for pdb to look at'}
    somedic['return_value'] = a_function_to_step_into(5,6)
    if USE_PDB: 
        import pdb;pdb.set_trace()
    return "<h1>flaskapp</h1><h2>Hello, PDB!</h2><p><a href='/'>Home page</a>.</p>"

@app.route("/")
def hello_world():
    d=datetime.now()
    fmtd_dttime = d.strftime('%Y%m%dT%H%M%S') #'outputs something like : 20120115T143929'
    return '''<h1>flaskapp</h1><h2>v1.0.0</h2><p>Page served at : ''' + fmtd_dttime + '''</p><p>If you want to try debugging <a href='/hellopdb'>click here</a>.</p>'''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
