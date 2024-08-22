from django.db import models


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
        verbose_name="Категория", help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name='products',
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Введите цену"
    )
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
        default=0
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "description"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование", help_text="Введите наименование",
    )
    description = models.TextField(
        max_length=100, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name



