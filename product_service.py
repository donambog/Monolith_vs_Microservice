from flask import Flask, jsonify

app = Flask(__name__)

products = [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
