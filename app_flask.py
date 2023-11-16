from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # render homepage
def home():
    return 'home page'


@app.route('/api', methods=['POST'])  # for calling api
def calculator():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if operation == 'add':
            res = num1 + num2
            result = f'sum of {str(num1)} and {str(num2)} is {str(res)}'

        if operation == 'subtract':
            res = num1 - num2
            result = f'difference of {str(num1)} and {str(num2)} is {str(res)}'

        if operation == 'multiply':
            res = num1 * num2
            result = f'product of {str(num1)} and {str(num2)} is {str(res)}'

        if operation == 'divide':
            res = num1 / num2
            result = f'division of {str(num1)} and {str(num2)} is {str(res)}'

        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)