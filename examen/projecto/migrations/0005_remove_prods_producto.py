# Generated by Django 4.1 on 2022-09-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projecto', '0004_rename_productos_prods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prods',
            name='producto',
        ),
    ]