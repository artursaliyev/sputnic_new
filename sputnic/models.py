from django.db import models
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.fields import JSONField
from django.urls import reverse


class RubricSputnic(models.Model):
    head = models.CharField(max_length=500, blank=True)
    sputnic = models.ForeignKey('Sputnic', on_delete=models.CASCADE, related_name='s_rubrics')


class ObjectSputnic(models.Model):
    type_o = models.CharField(max_length=100)
    name_o = models.CharField(max_length=100)
    rank_o = models.CharField(max_length=100)
    sputnic = models.ForeignKey('Sputnic', on_delete=models.CASCADE, related_name='s_objects')


class Sputnic(models.Model):
    title = models.TextField(blank=True)
    author = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=100, blank=True)
    time = models.CharField(max_length=100, blank=True)
    domain = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=500, blank=True)

    route_api = models.CharField(max_length=500, blank=True)
    heading = models.CharField(max_length=100, blank=True)
    date_get = models.CharField(max_length=100, blank=True)
    time_get = models.CharField(max_length=100, blank=True)

    search_vector = SearchVectorField(null=True)

    json_field = JSONField(null=True)

    class Meta:
        ordering = ['date_get']
        indexes = [
            GinIndex(fields=['search_vector'])
        ]

    def get_absolute_url(self):
        return reverse('sputnic:detail', args=(self.pk,))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if 'update_fields' not in kwargs or 'search_vector' not in kwargs['update_fields']:
            vector = SearchVector('title', config='russian') + \
                     SearchVector('description', config='russian')

            Sputnic.objects.filter(pk=self.pk).update(search_vector=vector)

