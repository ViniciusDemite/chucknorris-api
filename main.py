from flask import Flask, request, make_response, jsonify
import requests


BASE_URL = '/api/jokes'

app = Flask(__name__)
error_response = {
  'error': 'Not Found',
  'message': '',
}

@app.get(f'{BASE_URL}/random')
def random():
  joke = requests.get('https://api.chucknorris.io/jokes/random')

  return make_response(joke.json(), 200)

@app.get(f'{BASE_URL}/category/<string:name>')
def category(name):
  joke = requests.get(f'https://api.chucknorris.io/jokes/random?category={name}')

  if joke.status_code == 404:
    error_response['message'] = f'Não foi possível encontrar uma categoria com o nome: {name}'
    return make_response(jsonify(error_response), 404)

  return make_response(joke.json(), 200)

@app.get(f'{BASE_URL}/filter')
def filter():
  search = request.args.get('search')

  if search == None:
    error_response['error'] = 'Missing Param'
    error_response['message'] = 'É necessário utilizar o parâmetro "search" para buscar piadas'
    return make_response(jsonify(error_response), 400)

  try:
    limit = int(request.args.get('limit', default=10))
  except ValueError:
    error_response['error'] = 'Type Error'
    error_response['message'] = 'É necessário passar um valor inteiro no parâmetro "limit"'
    return make_response(jsonify(error_response), 400)

  response = requests.get(f'https://api.chucknorris.io/jokes/search?query={search}&limit={limit}')

  jokes = response.json()
  jokes_length = len(jokes['result'])

  if jokes_length == 0:
    error_response['message'] = f'Não foi possível encontrar nenhuma piada com o termo pesquisado: {search}'
    return make_response(jsonify(error_response), 404)

  results = {
    'limit': limit,
    'results': jokes['result'][:limit] if limit <= jokes_length else jokes['result']
  }

  return make_response(jsonify(results), 200)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port="5000")