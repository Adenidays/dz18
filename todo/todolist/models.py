from django.db import models
from django.urls import reverse


class TodoList(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    start_deadline = models.DateField()
    deadline = models.DateField()
    priority_choices = [
        ('low', 'Малый'),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    ]
    priority = models.CharField(max_length=10, choices=priority_choices)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_name}'

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Список задач"
        ordering = ['-start_deadline', '-priority']