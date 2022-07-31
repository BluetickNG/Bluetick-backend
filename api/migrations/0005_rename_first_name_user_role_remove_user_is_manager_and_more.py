# Generated by Django 4.0.5 on 2022-07-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_notifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='role',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_manager',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_super',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='invitation_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]