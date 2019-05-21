from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(blank=True, upload_to='%Y/%m/%d/img')
    file = models.FileField(blank=True, upload_to='%Y/%m/%d/file')
    #file = models.FileField(blank=True, upload_to='%Y/%m/%d/file')

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    def publish(self):
        self.save()

    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(primary_key=True)
    def publish(self, num):
        number = num
        self.save()

    def __str__(self):
        return self.name
