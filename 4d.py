@app.route('/products', methods=['GET'])
def list_products():
    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('available')
    
    query = Product.query
    if name:
        query = query.filter_by(name=name)
    if category:
        query = query.filter_by(category=category)
    if availability is not None:
        query = query.filter_by(availability=availability == 'true')
    
    products = query.all()
    return jsonify([product.serialize() for product in products]), 200
