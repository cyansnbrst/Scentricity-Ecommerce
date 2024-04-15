from store.models import Product, Brand, Category

class ProductTestDataMixin:
    @staticmethod
    def create_test_data():
        brand1 = Brand.objects.create(name='Brand A')
        brand2 = Brand.objects.create(name='Brand B')
        category1 = Category.objects.create(name='Perfumes')
        category2 = Category.objects.create(name='Candles')

        product1 = Product.objects.create(name='Perfume 1', brand=brand1, price=50.00, quantity=50,
                                               category=category1, image='None.jpeg')
        product2 = Product.objects.create(name='Perfume 2', brand=brand2, price=45.00, quantity=40,
                                               category=category1, image='None.jpeg')
        product3 = Product.objects.create(name='Candle 1', brand=brand1, price=50.00, quantity=60,
                                               category=category2, image='None.jpeg')
        product4 = Product.objects.create(name='Candle 2', brand=brand2, price=55.00, quantity=30,
                                               category=category2, image='None.jpeg')

        return [product1, product2, product3, product4]
