# Generated by Django 3.2.4 on 2021-07-23 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purbeurre', '0005_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='substitutes',
            name='user',
            field=models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='category_owner', to='purbeurre.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default=False, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutriscore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purbeurre.nutriscore'),
        ),
    ]
