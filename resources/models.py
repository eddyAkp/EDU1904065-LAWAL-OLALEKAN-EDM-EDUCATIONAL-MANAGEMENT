from django.db import models

# Create your models here.

MODE_OF_SERIALISATION: tuple = (
    ("Episode", "Episode"),
    ("Issue", "Issue"),
)


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)


class InformationMaterial(models.Model):
    title = models.CharField(max_length=1000, blank=False, null=False)
    quantity = models.PositiveIntegerField(default=1)
    price_per_unit = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class AudioVisualMaterial(InformationMaterial):
    pass


class PrintMediaMaterial(InformationMaterial):
    ISBN = models.CharField(max_length=30)
    publish_date = models.DateField(blank=True)


class SerialPrintMediaMaterial(PrintMediaMaterial):
    serialization_mode = models.CharField(
        choices=MODE_OF_SERIALISATION,
        null=False, blank=False, max_length=100,
    )
    serial = models.CharField(max_length=100)
