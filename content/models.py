from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	college = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	challenge_type = models.CharField(max_length=20)
	description = models.TextField()
	poster = models.ImageField(default='img.png')
	link = models.URLField(max_length=200)
	date = models.DateField()

	def __str__(self):
		return self.title