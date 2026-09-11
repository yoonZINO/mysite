from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    #image
    #tag
    #category
    #author
    counted_view = models.IntegerField(default=0) #deafult is 0
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return ('%i - %s') % (self.id, self.title)
        