from django.db import models
import django_tables2 as tables

class SubTask(models.Model):
	customer = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	title = models.CharField(max_length=50)
	platform = models.CharField(max_length=20)
	process = models.CharField(max_length=20)

	def __str__(self):
		return u'%s %s %s %s %s ' % (self.customer, self.description, self.title, 
			self.platform, self.process)

class Person(models.Model):
	name = models.CharField(verbose_name="full name", max_length=1000)
