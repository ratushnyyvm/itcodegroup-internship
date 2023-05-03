from django.db import models


# Create your models here.
class Material(models.Model):
    name = models.CharField('Наименование', max_length=255, unique=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.name


class Part(models.Model):
    designation = models.CharField('Обозначение', max_length=50, unique=True)
    name = models.CharField('Наименование', max_length=50)
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        related_name='parts',
        verbose_name='Материал'
    )
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        ordering = ('designation',)
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'

    def __str__(self):
        return f'{self.designation} - {self.name}'


class Assembly(models.Model):
    designation = models.CharField('Обозначение', max_length=50, unique=True)
    name = models.CharField('Наименование', max_length=50)
    parts = models.ManyToManyField(
        Part,
        blank=True,
        verbose_name='Детали'
    )
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        ordering = ('designation',)
        verbose_name = 'Сборка'
        verbose_name_plural = 'Сборки'

    def __str__(self):
        return f'{self.designation} - {self.name}'