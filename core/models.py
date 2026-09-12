from django.db import models

# Create your models here.
class BaseModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True