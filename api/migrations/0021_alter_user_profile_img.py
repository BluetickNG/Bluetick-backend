# Generated by Django 4.1.1 on 2022-10-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_img'),
        ),
    ]
