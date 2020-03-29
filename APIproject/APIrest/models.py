from django.db import models

# Create your models here.

class PGLlist(models.Model):
    Name        = models.CharField(max_length = 100)
    Position    = models.CharField(max_length = 100)
    Email       = models.EmailField(max_length = 200)

    def __str__(self):
        return self.Name

    class Meta:
        db_table = 'PGL'