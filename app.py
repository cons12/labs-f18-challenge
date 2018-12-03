from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/pokemon/<int:id>') 
def get_poke(id):
    r = requests.get("http://pokeapi.co/api/v2/pokemon/{}".format(id))
    jsonf = r.json()
    name = jsonf['name']
    return "<h1>The pokemon with id {} is {}</h1>".format(id,name)

@app.route('/pokemon/<string:name>')
def get_poke_name(name):
    r = requests.get("http://pokeapi.co/api/v2/pokemon/{}".format(name))
    jsonf = r.json()
    id = jsonf['id']
    return "<h1>{} has id {}</h1>".format(name.capitalize(),id)
    
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=7775, debug=True)