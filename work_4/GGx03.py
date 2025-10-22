from datetime import datetime

"""
учебный модуль в нём расставлены классы и функции:
    User - пользователь
    Admin - админ
    Product - продукт
    ShoppingCart - корзина
    Order - заказ
"""

"""
class Users ------------------------------------------------------------------------------------------------------------
"""


class PrimeUser:
    def __init__(self, name, *args, **kwargs):
        """
        шаблон для создания пользователей
        :param name: str
        :param args: any (не используется)
        :param kwargs: any (дополнительные данные)
        """
        self.name = name

        self.data = kwargs


class Admin(PrimeUser):
    def __init__(self, name, *args, **kwargs):
        """
        шаблон для создания админов
        :param name: str
        :param args: any (не используется)
        :param kwargs: any (дополнительные данные)

        level: str (admin)

        заготовка для админов на будущее
        """
        super().__init__(name, *args, **kwargs)

        self.level = "admin"
        self.history = dict()


class User(PrimeUser):
    def __init__(self, name, *args, **kwargs):
        """
                шаблон для создания админов
                :param name: str
                :param args: any (не используется)
                :param kwargs: any (дополнительные данные)

                level: str (user)

                иемеет история по заказов по дате
                """
        super().__init__(name, *args, **kwargs)

        self.level = "user"
        self.history = dict()

        self.shopping_cart = None
        self.order = None

    def create_shopping_cart(self):
        """
            создание корзины для пользователя
        :return: None
        """
        self.shopping_cart = ShoppingCart(self.name)

    def add_product(self, product):
        """
            добавление продукта в корзину
        :param product: ShoppingCart
        :return: None
        """
        assert isinstance(self.shopping_cart, ShoppingCart), "shopping cart is not created"
        self.shopping_cart += product

    def delete_product(self, product):
        """
            удаление продукта из корзины
        :param product: ShoppingCart
        :return: None
        """
        assert not self.shopping_cart, "shopping cart is not created"
        assert product not in self.shopping_cart, "product is not in shopping cart"

        self.shopping_cart -= product

    def set_shopping_cart(self):
        """
            создание корзины для пользователя
        :return: None
        """
        assert not self.shopping_cart, "shopping cart is not created"
        self.shopping_cart = ShoppingCart(self.name)

    def create_order(self):
        """
            создание заказа
        :return: self
        """
        self.order = Order(self.shopping_cart)
        return self

    def get_order(self):
        """
            получение заказа
        :return: self.order
        """
        assert isinstance(self.order, Order), "order is not created"
        if datetime.now() not in self.history:
            self.history[datetime.now()] = [self.order]
        else:
            self.history[datetime.now()].append(self.order)
        return self.order


"""
class Orders -----------------------------------------------------------------------------------------------------------
"""


class Product:
    def __init__(self, price, availability, category):
        """
            шаблон для создания продукта
        :param price: float
        :param availability: bool
        :param category: str
        """
        self.price = price
        self.category = category
        self.availability = availability


class ShoppingCart:
    def __init__(self, name_user, *args, **kwargs):
        """
            шаблон для создания корзины
        :param name_user: str
        :param args: any (не используется)
        :param kwargs: any (дополнительные данные) (не используется)

        работает с продуктами через + и -
        """
        self.date = datetime.now()
        self.name_user = name_user

        self.products = []

    @property
    def shopping_list(self):
        return self.products

    @shopping_list.setter
    def shopping_list(self, value):
        self.products = value

    def __add__(self, product):
        self.products.append(product)
        return self

    def __sub__(self, product):
        self.products.remove(product)
        return self


class Order:
    def __init__(self, shopping_cart, *args, **kwargs):
        """
            шаблон для создания заказа
        :param shopping_cart: ShoppingCart
        :param args: any (не используется)
        :param kwargs: any (не используется)
        """
        self.shopping_cart = shopping_cart
        self.price = self.get_price()

    def get_price(self):
        """
            получение цены заказа
        :return: float | int
        """
        products = self.shopping_cart.products
        return sum([product.price for product in products])

    def __str__(self):
        return f"price: {self.price}"


user = User("vlad")

product_1 = Product(100, True, "food")
product_2 = Product(200, True, "pen")

user.create_shopping_cart()

user.add_product(product_1)
user.add_product(product_2)

user.create_order()

answer = user.get_order()

print(answer)
print(*[product.category for product in user.shopping_cart.products])
print(user.history)

"""
    О, Python, наш цифровой кумир,
    Пусть User не знает ошибок и дыр!
    Когда create_shopping_cart дерзнёт создать,
    Да не посмеет программа упадать.

    При add_product и add магическом,
    Пусть продукты в корзине лежат логически.
    А когда create_order настанет пора,
    Пусть get_price посчитает sum() без стыда.

    От AssertionError корзины пустой,
    Спаси нас, о Python, святой и родной!
    И если в shopping_cart вдруг попадёт None,
    Дай сил нам пройти этот тернистый путь вновь.

    Аминь!
"""