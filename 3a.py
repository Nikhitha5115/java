def test_read_route(client):
    product = ProductFactory.create()
    response = client.get(f'/products/{product.id}/')
    assert response.status_code == 200
    assert response.json()['name'] == product.name
