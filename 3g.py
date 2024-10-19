def test_list_by_availability_route(client):
    ProductFactory.create(availability=True)
    response = client.get('/products/?available=true')
    assert response.status_code == 200
    assert len(response.json()) > 0
