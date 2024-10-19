def test_list_by_name_route(client):
    ProductFactory.create(name="TestProduct")
    response = client.get('/products/?name=TestProduct')
    assert response.status_code == 200
    assert response.json()[0]['name'] == "TestProduct"
