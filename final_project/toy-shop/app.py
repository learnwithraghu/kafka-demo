from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Toy 1", "price": 10.99, "image": "toy1.jpg"},
    {"id": 2, "name": "Toy 2", "price": 15.99, "image": "toy2.jpg"},
    {"id": 3, "name": "Toy 3", "price": 20.99, "image": "toy3.jpg"},
    {"id": 4, "name": "Toy 4", "price": 25.99, "image": "toy4.jpg"},
    {"id": 5, "name": "Toy 5", "price": 30.99, "image": "toy5.jpg"},
    {"id": 6, "name": "Toy 6", "price": 35.99, "image": "toy6.jpg"},
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/place_order', methods=['POST'])
def place_order():
    name = request.form['name']
    address = request.form['address']
    # Here you would typically send the order details to Kafka
    # For now, we'll just clear the cart and show a confirmation message
    cart.clear()
    return render_template('order.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)