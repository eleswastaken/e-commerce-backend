from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=250)
    
    slug            = models.CharField(max_length=50)

    parent_category = models.ForeignKey('api.Category', on_delete=models.DO_NOTHING, blank=True, null=True)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField()

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        self.last_modified = timezone.now()

        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name