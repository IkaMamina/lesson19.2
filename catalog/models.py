from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование",
    )
    description = models.TextField(
        max_length=100, verbose_name="Описание", help_text="Введите описание"
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    owner = models.ForeignKey(User, verbose_name="Поставщик", help_text="Укажите поставщика", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "description"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование",
    )
    description = models.TextField(
        max_length=100, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="продукт",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    number_version = models.IntegerField(verbose_name='номер версии', help_text='введите номер версии')
    name_version = models.CharField(max_length=50, verbose_name='название версии', help_text='введите название версии')
    current_version = models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return self.name_version

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
