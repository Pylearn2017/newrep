from django.db import models

class Bb(models.Model):

    rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = 'Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name =  'Объявление'
        ordering = ['-published']

    title = models.CharField(max_length = 50)
    content = models.TextField(null = True, blank = True)
    price = models.FloatField(null = True, blank = True)
    published = models.DateTimeField(auto_now_add = True, db_index = True)


class Rubric(models.Model):
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name =  'Рубрика'
        ordering = ['name']

    name = models.CharField(max_length = 20, db_index = True, verbose_name = 'Название рубрики')