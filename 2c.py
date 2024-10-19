def test_delete_product(db):
    product = ProductFactory.create()
    product_id = product.id
    product.delete()
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product_id)
