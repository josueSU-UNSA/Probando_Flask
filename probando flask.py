from flask import Flask
from flask import request
app = Flask(__name__) # instancia
# params followed by slashes
@app.route('/method2/') # accept 0 params
@app.route('/method2/<name>/') # one param
@app.route('/method2/<name>/<string:apellido>') # two params
#@app.route('/method4/<int:num>/<int:num1>/<int:num2>')
def method2(name='No data', apellido='sin datos '):
    return 'Hola ' + str (name) + ' ' + str (apellido)
#def method4(num='No num 1', num1='No num2',num2='No num 3'):
#    return int(num)/3+int(num1)/3+int(num2)/3
if __name__ == '__main__':
    app.run(debug=True, port=8080) # lunch server
