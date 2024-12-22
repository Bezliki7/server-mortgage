from flask import Blueprint, render_template, request


class MainController:
    def __init__(self):
        self.main_bp = Blueprint('main_bp', __name__)
        self.setup_routes()

    def setup_routes(self):
        @self.main_bp.get("/")
        def home():
            return render_template('index.html', monthly_payment=None, minimum_salary=None)
        
        @self.main_bp.post('/')
        def calculate():
                principal = float(request.form['principal'])
                annual_rate = float(request.form['annual_rate']) / 100
                years = int(request.form['years'])

                monthly_rate = annual_rate / 12
                number_of_payments = years * 12
                monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)

                percentage_of_income = 0.28 
                minimum_salary = monthly_payment / percentage_of_income
                return render_template('index.html', monthly_payment=monthly_payment, minimum_salary=minimum_salary)


