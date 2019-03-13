from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    def __str__(self):
        return self.first_name + " " + self.last_name


class Article(models.Model):
    title = models.CharField(max_length=120)
    abstract = models.TextField(max_length=120)
    article = models.TextField()
    author = models.ForeignKey(
    Author,
    on_delete=models.CASCADE,
    verbose_name="the author")

    def get_average_rating(self):
        sum = 0
        for rating in self.rating_set.all():
            sum += rating.value
        return sum/self.rating_set.count()

    def __str__(self):
        return self.title



class Rating(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="The rated article",
    )
    rating = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
    def __str__(self):
        return "Rating: " + str(self.rating) + " for artikkel: " + str(self.article)
