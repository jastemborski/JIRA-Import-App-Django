from django.db import models
import django_tables2 as tables

class SubTask(models.Model):
	customer = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	title = models.CharField(max_length=50)
	platform = models.CharField(max_length=20)
	process = models.CharField(max_length=20)
	notes = models.CharField(blank=True, max_length=300)

	def __str__(self):
		return u'%s %s %s %s %s ' % (self.customer, self.description, self.title, 
			self.platform, self.process)
# Create your models here.23
