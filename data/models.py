from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, DecimalValidator
from taggit.managers import TaggableManager


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    name = models.CharField('Название', max_length=100, default='Продукт', validators=[
        RegexValidator(
            regex=r'\.$',
            message='уберите точку!',
            inverse_match=True,
        )
    ])
    img = models.ImageField('Картинка', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=True, validators=[
        DecimalValidator(
            max_digits=8,
            decimal_places=2,
        )
    ])
    description = models.TextField('Описание')
    are_available = models.BooleanField('имеется в наличии', default=True)
    amount = models.IntegerField('Количество товара')
    tags = TaggableManager()

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField('Категория', max_length=100, validators=[
        RegexValidator(
            regex=r'\.$',
            message='уберите точку!',
            inverse_match=True,
        )
    ])
    img = models.ImageField('Картинка', blank=True, null=True)
    prod = models.ManyToManyField(Product, verbose_name='Продукты', related_name='category_detail')

    def __str__(self):
        return f'{self.title}'


class Discount(models.Model):

    class Meta:
        verbose_name = 'Скидкa'
        verbose_name_plural = 'Скидки'

    discount = models.IntegerField('Скидка', blank=True, null=True, validators=[
        MinValueValidator(
            limit_value=1,
            message='Не менее 1!'
        )
    ])
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='discount_detail')

    def __str__(self):
        return f'{self.discount}'


class TheSize(models.Model):

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = "Размеры"

    title = models.CharField('Размер', max_length=6)
    prod = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Размер', related_name='prod_detail')

    def __str__(self):
        return f'{self.title}'


class Color(models.Model):

    class Meta:
        verbose_name = 'Расцветка'
        verbose_name_plural = 'Расцветки'

    color = models.ImageField('расцветки', blank=True, null=True)
    color_name = models.CharField('Цвет', max_length=100)
    prod = models.ForeignKey(Product, on_delete=models.PROTECT,  verbose_name='расцветки', related_name='product_detail')

    def __str__(self):
        return f'{self.color_name}'


class Recommendations(models.Model):
    name = models.CharField('Название', max_length=100)
    products = models.ManyToManyField(Product, verbose_name='Продукт', related_name='recommendations_detail')

    class Meta:
        verbose_name = 'рекомендация'
        verbose_name_plural = 'рекомендации'

    def __str__(self):
        return f'{self.name}'


DELIVERY = (('1', 'Доставка курьером'),
            ('2', 'самовывоз'),)

CITY = (
    ('1', 'Чуй'),
    ('2', 'Бишкек'),
    ('3', 'Ош'),
    ('4', 'Талас'),
    ('5', 'Иссык куль'),
    ('6', 'Джалал абад'),
    ('7', 'Баткен'),
)


class Ordering(models.Model):

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'

    full_name = models.CharField('Фио', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=20)
    region = models.CharField(choices=CITY, verbose_name='Область', max_length=100)

    def __str__(self):
        return f'{self.full_name}'


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'

    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    address = models.ForeignKey(Ordering, on_delete=models.CASCADE, verbose_name='Адрес')

    def __str__(self):
        return f'{self.address}'


class ChoiceOrder(models.Model):

    class Meta:
        verbose_name = 'Выбор заказа'
        verbose_name_plural = 'Выбор заказов'

    shop = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='choice_order_detail')

    def __str__(self):
        return f'{self.order}'
