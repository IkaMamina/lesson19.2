# Generated by Django 4.2.2 on 2024-09-18 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category", "description"],
                "permissions": [
                    ("can_edit_category", "Can edit category"),
                    ("can_edit_description", "Can edit description"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
