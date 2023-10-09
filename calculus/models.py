from djongo import models


class Calculate(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
