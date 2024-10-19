def test_list_all_route(client):
    ProductFactory.create_batch(3)
    response = client.get('/products/')
    assert response.status_code == 200
    assert len(response.json()) == 3
