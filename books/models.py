from django.db import models

class Publisher(models.Model):
	name = models.CharField(max_length=1024)
	address1 = models.CharField(max_length=100)
	address2 = models.CharField(max_length=100)


class Book(models.Model):
	title = models.CharField(max_length=1024)
	isbn = models.CharField(max_length=13, unique=True)
	description = models.TextField()
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publish_date = models.DateTimeField()
	language = models.CharField(max_length=20)


