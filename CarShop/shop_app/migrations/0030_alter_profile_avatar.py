# Generated by Django 4.2.1 on 2023-08-13 23:08

from django.db import migrations
import shop_app.overwrite_storage


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0029_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=shop_app.overwrite_storage.AvatarField(blank=True, default='profile_avatars/avatar_default.jpg', null=True, storage=shop_app.overwrite_storage.OverwriteCodedStorage(), upload_to='profile_avatars'),
        ),
    ]
