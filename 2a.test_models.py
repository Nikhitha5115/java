def test_read_product(db):
    product = ProductFactory.create()
    fetched_product = Product.objects.get(id=product.id)
    assert fetched_product.name == product.name
