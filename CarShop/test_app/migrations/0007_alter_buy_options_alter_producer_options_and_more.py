# Generated by Django 4.2.1 on 2023-07-15 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_rename_bye_buy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buy',
            options={'verbose_name': 'Buy', 'verbose_name_plural': 'Buys'},
        ),
        migrations.AlterModelOptions(
            name='producer',
            options={'verbose_name': 'Producer', 'verbose_name_plural': 'Producers'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'Product type', 'verbose_name_plural': 'Product types'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'Provider', 'verbose_name_plural': 'Providers'},
        ),
    ]
