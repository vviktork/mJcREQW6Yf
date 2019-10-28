from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


class Functions(models.Model):
    formula = models.CharField(max_length=10, verbose_name='Функции')

    def __str__(self):
        return self.formula

    class Meta:
        verbose_name = 'Функция'
        verbose_name_plural = 'Функции'
        ordering = ['formula']


class Common(models.Model):
    formula = models.ForeignKey(Functions, on_delete=models.CASCADE,
                                verbose_name='Функция'
                                )
    images = models.ImageField(blank=True, null=True,
                              upload_to='image',
                              help_text='150x150px',
                              verbose_name='График'
                              )
    interval = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)],
                                                default=1,
                                                verbose_name='Интервал t, дней'
                                                )
    dt = models.IntegerField(validators=[MinValueValidator(1)],
                             default=1,
                             verbose_name='Шаг t, часы'
                             )
    time = models.DateTimeField(auto_now=True, auto_now_add=False,
                                verbose_name='Дата обработки',
                                )

    def __str__(self):
        return '{}'.format(self.formula)

    def image_img(self):
        if self.images:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.images.url))
        else:
            return 'Большой шаг для интервала или функция неизвестна'

    image_img.short_description = 'График'
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'Графики'
        ordering = ['formula']
