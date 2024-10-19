def test_update_route(client):
    product = ProductFactory.create()
    response = client.put(f'/products/{product.id}/', data={'name': 'Updated Name'})
    assert response.status_code == 200
    updated_product = Product.objects.get(id=product.id)
    assert updated_product.name == 'Updated Name'
