from django.db import models

# Create your models here.
class Link(models.Model):
    def __str__(self):
        return self.name

    # null and black are all True is because there are no appropriate links/address for certain links
    # inorder to avoid any errors, we just set them as True
    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)