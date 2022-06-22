from flask import Flask, Response, request
import requests

BASE_URL = '/api/jokes'

app = Flask(__name__)

@app.get(f'{BASE_URL}/random')
def random():
  response = requests.get('https://api.chucknorris.io/jokes/random')

  return Response(response.json(), status=200, mimetype='application/json')

@app.get(f'{BASE_URL}/category/<string:name>')
def category(name):
  response = requests.get(f'https://api.chucknorris.io/jokes/random?category={name}')

  if response.status_code == 404:
    return Response(status=404, mimetype='application/json')

  return Response(response.json(), status=200, mimetype='application/json')

@app.get(f'{BASE_URL}/filter')
def filter():
  search = request.args.get('search')
  limit = request.args.get('limit', default=10)

  if search == None:
    return Response(status=400, mimetype='application/json')

  response = requests.get(f'https://api.chucknorris.io/jokes/search?query={search}&limit={limit}')

  if response.status_code == 404:
    return Response(status=404, mimetype='application/json')

  return Response(response.json(), status=200, mimetype='application/json')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port="5000")