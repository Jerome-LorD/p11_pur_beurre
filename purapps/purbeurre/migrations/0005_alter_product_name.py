# Generated by Django 3.2.4 on 2021-07-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0004_auto_20210712_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=False, max_length=180, unique=True),
        ),
    ]