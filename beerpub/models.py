from django.db import models
from django.urls import reverse


class Beer(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование пива')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Информация о пиве  ')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Вид пива')

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Лучшее пиво'
        verbose_name_plural = 'Лучшее пиво'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Разновидность пива')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'виды пива'
        verbose_name_plural = 'Виды пива'
        ordering = ['id']
