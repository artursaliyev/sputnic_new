from django.db import models


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

    class Meta:
        ordering = ['date', ]
        index_together = ('title', 'author', 'description', 'date', 'time', 'domain', 'url')



