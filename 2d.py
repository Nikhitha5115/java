def test_list_all_products(db):
    ProductFactory.create_batch(3)
    all_products = Product.objects.all()
    assert len(all_products) == 3
