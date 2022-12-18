from django.db import models

# Create your models here.


EDITIONS = (
    ("Revised", "Revised"),
    ("First", "First"),
    ("Second", "Second"),
    ("Third", "Third"),
    ("Fourth", "Fourth"),
    ("Fifth", "Fifth"),
    ("Sixth", "Sixth"),
    ("Seventh", "Seventh"),
)  # TODO: Generator for editions from 1 -> 100


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.name}'


class InformationMaterial(models.Model):  # Base Class
    title = models.CharField(max_length=1000, blank=False, null=False)
    quantity = models.PositiveIntegerField(default=1)
    price_per_unit = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.title}, {self.author.name} '


class AudioVisualMaterial(InformationMaterial):
    objects = models.Manager()

    def __str__(self) -> str:
        return super().__str__()


class PrintMediaMaterial(InformationMaterial):
    ISBN = models.CharField(max_length=30)
    publish_date = models.DateField(blank=True)
    edition = models.CharField(max_length=100, choices=EDITIONS, blank=True)

    objects = models.Manager()

    def __str__(self) -> str:
        return super().__str__() + f'{self.ISBN}'


class SerialMaterial(InformationMaterial):
    ISSN = models.CharField(max_length=30, blank=True)
    issue_number = models.PositiveIntegerField()
    volume_number = models.PositiveIntegerField()
    publish_date = models.DateField(blank=True)

    objects = models.Manager()

    def serialization_display(self) -> str:
        """
        Return serialization mode and serial information.
        Example:
            SerialPrintMediaMaterial("Issue", "1").serialization_display()
            returns "Issue 1"
        """
        return 'Volume ' + self.volume_number + " Issue " + self.issue_number

    def __str__(self) -> str:
        return super().__str__() + f'{self.serialization_display}'
