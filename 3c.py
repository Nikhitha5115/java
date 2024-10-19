def test_delete_route(client):
    product = ProductFactory.create()
    response = client.delete(f'/products/{product.id}/')
    assert response.status_code == 204
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product.id)
