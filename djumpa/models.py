from django.db import models

class Djumpa(models.Model):
    referer     = models.URLField(null=True, blank=True)
    redirect    = models.URLField()
    sessionid   = models.CharField(max_length=32)
    rank        = models.PositiveSmallIntegerField(null=True, blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)