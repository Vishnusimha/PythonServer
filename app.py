from flask import Flask, jsonify, request

app = Flask(__name__)

# Define the version
VERSION = "v2"

# Endpoint returning a JSON response
@app.route('/json', methods=['GET'])
def get_json():
    data = {'message': f'Hello, this is a JSON response! Version: {VERSION}'}
    return jsonify(data)

# Endpoint with path parameter
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f'Hello, {name}! Version: {VERSION}'

# Endpoint handling POST request with JSON data
@app.route('/post_data', methods=['POST'])
def post_data():
    req_data = request.get_json()
    return jsonify({'received_data': req_data, 'version': VERSION})

# Endpoint returning HTML response
@app.route('/html', methods=['GET'])
def get_html():
    html_content = f'<h1>Hello, this is an HTML response! Version: {VERSION}</h1>'
    return html_content, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)
