def test_find_by_category(db):
    ProductFactory.create(category="Books")
    products = Product.objects.filter(category="Books")
    assert len(products) > 0
