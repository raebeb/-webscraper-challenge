# Generated by Django 3.2.14 on 2022-08-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220802_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='stock',
            field=models.CharField(max_length=50),
        ),
    ]