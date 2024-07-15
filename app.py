from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
NEWS_API_KEY = 'c6a8a06a2ebf4073a48d7403c48ea845'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    query = request.args.get('q')
    category = request.args.get('category')
    params = {
        'apiKey': NEWS_API_KEY,
        'country': 'in',
        'pageSize': 20
    }
    if query:
        params['q'] = query
    if category and category != 'all':
        params['category'] = category

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()
    return jsonify(data)

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email')
    with open('emails.txt', 'a') as f:
        f.write(email + '\n')
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
