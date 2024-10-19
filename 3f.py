def test_list_by_category_route(client):
    ProductFactory.create(category="Electronics")
    response = client.get('/products/?category=Electronics')
    assert response.status_code == 200
    assert len(response.json()) > 0
