from django.db import models

class Lugat(models.Model):

	english = models.CharField('English', max_length=128)
	uzbek = models.CharField('Uzbek', max_length=128)