# Generated by Django 3.2.4 on 2021-09-12 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0015_product_user_url_unique'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='product',
            name='user_url_unique',
        ),
    ]
