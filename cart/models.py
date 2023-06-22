from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=50, unique=True)
    total_items = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)