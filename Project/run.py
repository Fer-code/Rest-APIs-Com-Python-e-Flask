from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def ola():
    return "Szia világ, minden, jól napot!"

#condição para apenas essa classe poder chamar
if __name__ == "__main__":
    app.run(debug=True) #'debug=True' vai reiniciar sozinho seu projeto, podendo alterar qqlr coisa sem restart
   