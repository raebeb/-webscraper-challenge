# Generated by Django 3.2.14 on 2022-07-31 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('cover', models.CharField(max_length=50)),
                ('upc', models.CharField(max_length=50)),
                ('product_type', models.CharField(max_length=50)),
                ('price_excl_tax', models.FloatField()),
                ('price_incl_tax', models.FloatField()),
                ('tax', models.FloatField()),
                ('availability', models.CharField(max_length=50)),
                ('number_of_reviews', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
