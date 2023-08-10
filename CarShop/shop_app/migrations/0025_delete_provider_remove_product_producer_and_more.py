# Generated by Django 4.2.1 on 2023-08-09 16:13

from django.conf import settings
from django.db import migrations
import shop_app.m2m_validation


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_app', '0024_alter_product_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Provider',
        ),
        migrations.RemoveField(
            model_name='product',
            name='producer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='providers',
        ),
        migrations.AddField(
            model_name='product',
            name='providers1',
            field=shop_app.m2m_validation.ChoicesValidatedManyToManyField(help_text='Select a provider for this product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Producer',
        ),
    ]
