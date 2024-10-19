def test_find_by_availability(db):
    ProductFactory.create(availability=True)
    available_products = Product.objects.filter(availability=True)
    assert len(available_products) > 0
