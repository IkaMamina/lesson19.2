from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="введите наименование",
    )
    description = models.TextField(
        max_length=100, verbose_name="описание", help_text="введите описание"
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="фото",
        help_text="загрузите фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="категория", help_text="введите категорию продукта",
        blank=True,
        null=True,
        related_name='products',
    )
    price = models.IntegerField(
        verbose_name="цена", help_text="введите цену"
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата создания",
        help_text="введите дату создания",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата последнего изменения",
        help_text="введите дату последнего изменения",
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
        verbose_name="наименование", help_text="введите наименование",
    )
    description = models.TextField(
        max_length=100, verbose_name="описание", help_text="введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


