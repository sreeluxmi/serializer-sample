from djongo import models
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=150)
    number_of_pages = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Series(models.Model):  
    book = models.EmbeddedField(
        model_container=Book
    )
    seriesName = models.CharField(max_length=150)
