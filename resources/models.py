from django.db import models

# Create your models here.

MODE_OF_SERIALISATION: tuple = (
    ("Episode", "Episode"),
    ("Issue", "Issue"),
)


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    objects = models.Manager()

    def __str__(self) -> str:
        return f'{self.name}'


class InformationMaterial(models.Model):
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

    objects = models.Manager()

    def __str__(self) -> str:
        return super().__str__() + f'{self.ISBN}'


class SerialPrintMediaMaterial(PrintMediaMaterial):
    serialization_mode = models.CharField(
        choices=MODE_OF_SERIALISATION,
        null=False, blank=False, max_length=100,
    )
    serial = models.CharField(max_length=100)

    objects = models.Manager()

    def serialization_display(self) -> str:
        """
        Return serialization mode and serial information.
        Example:
            SerialPrintMediaMaterial("Issue", "1").serialization_display()
            returns "Issue 1"
        """
        return self.serialization_mode + " " + self.serial

    def __str__(self) -> str:
        return super().__str__() + f'{self.serialization_display}'
