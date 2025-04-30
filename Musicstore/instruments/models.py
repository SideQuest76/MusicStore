from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    instrument_type = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='instrument_photos/')

    def __str__(self):
        return self.name

class Order(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.instrument.name} by {self.customer_name}"
