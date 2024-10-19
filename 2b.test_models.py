def test_update_product(db):
    product = ProductFactory.create()
    product.name = "New Product Name"
    product.save()
    updated_product = Product.objects.get(id=product.id)
    assert updated_product.name == "New Product Name"
