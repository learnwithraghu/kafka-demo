# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime, timedelta
import json

app = Flask(__name__)
app.secret_key = 'demo_secret_key'  # Required for flash messages

# Product catalog
PRODUCTS = {
    'image_1': {
        'name': 'Teddy Bear',
        'price': 19.99,
        'description': 'Soft and cuddly teddy bear',
        'image': 'image_1.jpg'
    },
    'image_2': {
        'name': 'Toy Car',
        'price': 14.99,
        'description': 'Remote controlled toy car',
        'image': 'image_2.jpg'
    },
    'image_3': {
        'name': 'Dinosaur',
        'price': 24.99,
        'description': 'Realistic toy dinosaur',
        'image': 'image_3.jpg'
    },
    'image_4': {
        'name': 'Airplane',
        'price': 29.99,
        'description': 'Model airplane',
        'image': 'image_4.jpg'
    },
    'image_6': {
        'name': 'Duck',
        'price': 9.99,
        'description': 'Rubber duck toy',
        'image': 'image_6.jpg'
    },
    'image_7': {
        'name': 'Puzzle',
        'price': 19.99,
        'description': '100-piece puzzle',
        'image': 'image_7.jpg'
    }
}

# Shopping cart to store items
shopping_cart = {}

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/add_to_cart/<product_id>', methods=['POST'])
def add_to_cart(product_id):
    if product_id in PRODUCTS:
        if product_id not in shopping_cart:
            shopping_cart[product_id] = 1
        else:
            shopping_cart[product_id] += 1
        flash(f'{PRODUCTS[product_id]["name"]} added to cart!')
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart_items = {}
    total = 0
    for product_id, quantity in shopping_cart.items():
        product = PRODUCTS[product_id]
        cart_items[product_id] = {
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity,
            'subtotal': product['price'] * quantity
        }
        total += cart_items[product_id]['subtotal']
    
    # Calculate estimated delivery date (3 days from now)
    delivery_date = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
    
    return render_template('cart.html', cart_items=cart_items, total=total, delivery_date=delivery_date)

@app.route('/place_order', methods=['POST'])
def place_order():
    if not shopping_cart:
        flash('Your cart is empty!')
        return redirect(url_for('view_cart'))
    
    # Clear the cart after order is placed
    shopping_cart.clear()
    flash('Order placed successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)