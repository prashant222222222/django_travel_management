# Generated by Django 2.2.6 on 2019-10-26 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191026_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
    ]
