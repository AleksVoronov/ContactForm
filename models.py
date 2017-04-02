from django.db import models
from django.utils import timezone

#Модель обратной связи
class Contact(models.Model):
	class Meta():
		db_table = 'contact'
		verbose_name = "Обратная связь"
		verbose_name_plural = "Обратная связь"
	
	name = models.CharField("Имя", max_length=30)
	second_name = models.CharField("Фамилия", max_length=30)
	email = models.EmailField(max_length=70)
	message = models.TextField("Сообщение", max_length=1000)
	data = models.DateTimeField("Дата отправки", default=timezone.now)
	
	def __str__(self):
		return self.name