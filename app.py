from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to My Flask Web App"

# About route
@app.route('/about')
def about():
    return "This is the About Page"

# Dynamic route
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

# POST request route
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({
        "message": "Data received successfully",
        "data": data
    })

# Run the server
if __name__ == '__main__':
    app.run(debug=True)