# Generated by Django 3.2.4 on 2021-07-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0008_product_nutriments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='nutriments',
            field=models.CharField(blank=True, default=False, max_length=255),
        ),
    ]
