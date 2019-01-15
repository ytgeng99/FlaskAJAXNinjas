from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<color>')
def display(color):
    if color == 'red':
        return jsonify(img = 'raphael.jpg', text = 'You chose Raphael!')
    elif color == 'blue':
        return jsonify(img = 'leonardo.jpg', text = 'You chose Leonardo!')
    elif color == 'orange':
        return jsonify(img = 'michelangelo.jpg', text = 'You chose Michelangelo!')
    elif color == 'purple':
        return jsonify(img = 'donatello.jpg', text = 'You chose Donatello!')
    else:
        return jsonify(img = 'notapril.jpg', text = 'There\'s no ninja in that color!')

app.run(debug=True)