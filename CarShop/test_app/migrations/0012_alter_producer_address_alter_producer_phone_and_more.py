# Generated by Django 4.2.1 on 2023-07-25 22:49

from django.db import migrations, models
import test_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0011_alter_provider_address_alter_provider_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producer',
            name='address',
            field=models.CharField(max_length=64, validators=[test_app.validators.FullMatchRegexValidator('((\\b([A-Za-z]+)\\b)|(\\b([\\d\\.\\-]+)\\b)|([\\s,\\.\\:\\!]*))*', 'Address is incorrect. It must consist of words, numbers and codes.', code='invalid')]),
        ),
        migrations.AlterField(
            model_name='producer',
            name='phone',
            field=models.CharField(max_length=64, validators=[test_app.validators.FullMatchRegexValidator('\\+375\\s*\\(\\s*29\\s*\\)\\s*\\d{3}\\s*-\\s*\\d{2}\\s*-\\s*\\d{2}', 'Phone number is incorrect. Correct format is +375 (29) XXX-XX-XX.', code='invalid')]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='address',
            field=models.CharField(max_length=64, validators=[test_app.validators.FullMatchRegexValidator('((\\b([A-Za-z]+)\\b)|(\\b([\\d\\.\\-]+)\\b)|([\\s,\\.\\:\\!]*))*', 'Address is incorrect. It must consist of words, numbers and codes.', code='invalid')]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.CharField(max_length=64, validators=[test_app.validators.FullMatchRegexValidator('\\+375\\s*\\(\\s*29\\s*\\)\\s*\\d{3}\\s*-\\s*\\d{2}\\s*-\\s*\\d{2}', 'Phone number is incorrect. Correct format is +375 (29) XXX-XX-XX.', code='invalid')]),
        ),
    ]
