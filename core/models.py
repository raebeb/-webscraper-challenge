from django.db import models

# Create your models here.
class Book(models.Model):
    """Model definition for Book."""

    title = models.CharField(max_length=300)
    price = models.CharField(max_length=200)
    stock = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
    upc = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    price_excl_tax = models.CharField(max_length=200)
    price_incl_tax = models.CharField(max_length=200)
    tax = models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    number_of_reviews = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'
