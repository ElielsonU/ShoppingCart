# Generated by Django 4.1.7 on 2023-03-20 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='created_id',
            new_name='created_in',
        ),
    ]