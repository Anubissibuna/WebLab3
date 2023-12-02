from django.db import models

class Articles(models.Model):
	title = models.CharField('Название статьи', max_length = 50)
	text = models.CharField('Текст статьи', max_length = 5000)
	date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
