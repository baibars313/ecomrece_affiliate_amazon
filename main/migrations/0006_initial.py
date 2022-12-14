# Generated by Django 4.1.1 on 2022-09-28 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0005_remove_products_category_delete_category_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=100)),
                ("cat_slug", models.CharField(max_length=100, null=True)),
                ("category_description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("product_link", models.CharField(max_length=255, null=True)),
                ("price", models.CharField(max_length=255)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.category"
                    ),
                ),
            ],
        ),
    ]
