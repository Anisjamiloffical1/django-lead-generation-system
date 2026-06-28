from django.db import models

# Create your models here.
class Lead(models.Model):
    company_name = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.company_name
