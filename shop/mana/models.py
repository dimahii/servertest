from django.db import models
from django.utils import timezone


# Create your models here.

class Customers(models.Model):
	Choices = (
		(1,('درحال تعمیر')),
		(2,('تعمیر شده')),
		(3,('عدم امکان تعمیر'))
	)
	customer_name = models.CharField( max_length = 200 )
	customer_lastname = models.CharField( max_length = 200 )
	service_type = models.IntegerField( choices=Choices , default=1)
	service_date = models.DateTimeField(default=timezone.now())
	customer_id = models.IntegerField()
	phone_number = models.IntegerField()
	description = models.CharField ( max_length = 400 )


	def __str__(self):
		return self.customer_name
