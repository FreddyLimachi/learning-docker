
from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/')
def ping():
    return jsonify({"message": "server running"})

@app.route('/products')
def productos():
    return jsonify({"mensaje":"Lista de productos","products":products})

@app.route('/productos/<producto>')
def getProducto(producto):
    productito=0
    for i in products:
        if i['name'] == producto:
            productito=i
    if productito != 0:
        return jsonify({"products": productito})
    else: 
        return jsonify({"message": "product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product={
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
        }

    products.append(new_product)

    return jsonify({'message': "product added succesfully", "products": products})

@app.route('/products/<string:producto>', methods=['PUT'])
def edit_product(producto):
    productito=0
    for i in products:
        if i['name'] == producto:
            productito=i
    if productito != 0:
        productito[0]['name'] = request.json['name']
        productito[0]['price'] = request.json['price']
        productito[0]['quantity'] = request.json['quantity']
        return jsonify({"message": "producto updated",
            "product": productito[0]})
    else: 
        return jsonify({"message": "product not found"})


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)