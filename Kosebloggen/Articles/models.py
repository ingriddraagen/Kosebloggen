from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    abstract = models.TextField(max_length=120)
    article = models.TextField()
    author = models.ForeignKey(
    on_delete=models.CASCADE,
    verbose_name="the author")

    def get_average_rating(self):
        sum = 0
        for rating in self.rating_set.all():
            sum += rating.value
        return sum/self.rating_set.count()


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)


class Rating(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="The rated article",
    )
    rating = IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )
