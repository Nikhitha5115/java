import factory
from myapp.models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    category = factory.Faker('random_element', elements=['Electronics', 'Clothing', 'Books'])
    price = factory.Faker('random_number', digits=5)
    availability = factory.Faker('boolean')
