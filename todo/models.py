from django.db import models


class Task(models.Model):
    """Модель задачи в списке дел."""
    title = models.CharField('Загловок', max_length=100)
    text = models.TextField('Опимание')
    create_at = models.DateTimeField('Дата добавления', auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
