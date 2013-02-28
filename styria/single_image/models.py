from django.db import models
from django.db.models import Avg


class Image(models.Model):
    image_file = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200, null=True, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time_added', )

    def __unicode__(self):
        return self.description
    

class Comment(models.Model):
    text = models.TextField()
    image = models.ForeignKey(Image)
    time_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time_commented',)

    def __unicode__(self):
        return self.text


class Rating(models.Model):
    RATINGS = [(i, i) for i in range(6)]

    image = models.ForeignKey(Image)
    rating = models.IntegerField(choices=RATINGS)
    time_rated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time_rated',)

    def __unicode__(self):
        return str(self.rating)
