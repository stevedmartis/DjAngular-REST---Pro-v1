
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import render, get_object_or_404, redirect
from .utils import unique_slug_generator

from django.contrib.auth.models import User
from django.conf import settings



class Party(models.Model):
	name   		= models.CharField(max_length=220)
	description  = models.CharField(max_length=220)
	slug        = models.SlugField(unique=True, blank=True)
	createdAt   = models.DateTimeField(auto_now_add=True)
	updatedAt   = models.DateTimeField(auto_now_add=True)
	status		= models.ForeignKey("Status", on_delete=models.CASCADE)
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	place		= models.CharField(max_length=300)
	address		= models.CharField(max_length=200)
	location	= models.CharField(max_length=200)
	eventdate	= models.DateTimeField()
	category	= models.ForeignKey("Category", on_delete=models.CASCADE)
	tipo		= models.ManyToManyField("Tipo")



	def __str__(self): # __unicode__
		return self.name

	@property
	def title(self):
		return self.name


def partys_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(partys_pre_save_receiver, sender=Party)



class Status(models.Model):
	name   = models.CharField(max_length=20)

	def __str__(self): # __unicode__
		return self.name


class Category(models.Model):
	name   = models.CharField(max_length=20)

	def __str__(self): # __unicode__
		return self.name

class Tipo(models.Model):
	name   = models.CharField(max_length=20)

	def __str__(self): # __unicode__
		return self.name



