# Generated by Django 3.2.14 on 2022-08-02 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='price_excl_tax',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='price_incl_tax',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='tax',
            field=models.CharField(max_length=50),
        ),
    ]
