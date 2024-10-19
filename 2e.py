def test_find_by_name(db):
    product = ProductFactory.create(name="UniqueProductName")
    found_product = Product.objects.get(name="UniqueProductName")
    assert found_product.id == product.id
