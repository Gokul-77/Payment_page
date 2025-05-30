from django.db import models

class PaymentDetail(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    card_number = models.CharField(max_length=19)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=4)
    mob_number = models.CharField(max_length=10, blank=True)  
    billing_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.full_name}"
