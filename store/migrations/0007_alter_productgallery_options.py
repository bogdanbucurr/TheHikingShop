# Generated by Django 4.1.3 on 2023-01-16 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_productcgallery_productgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productgallery',
            options={'verbose_name': 'product gallery', 'verbose_name_plural': 'product gallery'},
        ),
    ]
