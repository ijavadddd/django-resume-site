from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    message = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
