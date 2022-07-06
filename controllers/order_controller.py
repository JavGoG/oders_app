from flask import render_template
from app import app
from models.orders import orders

@app.route('/')
def index():
    return render_template('index.html', title='Home', all_orders=orders)

@app.route ('/orders/index')
def method():
    return render_template('order.html', title='Home', all_orders=orders)
    
