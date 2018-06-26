from django.db import models

# Create your models here.
class Headlines(models.Model):
    title = models.CharField('Title', max_length=200, null=False)
    link = models.CharField('Link', max_length=200, null=False)
    time_added = models.DateTimeField('Time Added')
    author = models.CharField('Author', max_length=200)
    published = models.CharField('Published', max_length=200)

    def __str__(self):
        return f'{self.title} - {self.author}'
