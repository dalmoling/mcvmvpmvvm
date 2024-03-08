# main_app.py
from flask import Flask, render_template, request

app = Flask(__name__)

class CalculatorModel:
    def calculate(self, num1, num2, operator):
        if operator == 'add':
            return num1 + num2
        elif operator == 'subtract':
            return num1 - num2
        elif operator == 'multiply':
            return num1 * num2
        elif operator == 'divide':
            if num2 != 0:
                return num1 / num2
            else:
                return 'Error: Division by zero'

class CalculatorView:
    def render(self, result):
        return render_template('index.html', result=result)

class CalculatorPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def perform_calculation(self, num1, num2, operator):
        result = self.model.calculate(num1, num2, operator)
        return self.view.render(result)

model = CalculatorModel()
view = CalculatorView()
presenter = CalculatorPresenter(model, view)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operator = request.form['operator']
    return presenter.perform_calculation(num1, num2, operator)

if __name__ == '__main__':
    app.run(debug=True)
