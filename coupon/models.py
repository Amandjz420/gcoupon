from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class Tag(models.Model):

    name = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=50, blank=True)
    weight = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-weight']

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)


    def save(self, *args, **kwargs):
        if not self.code:
            code = self.name.replace(' ', '')
            code = code.replace('-', '')
            self.code = code.lower()
        if not self.color:
            self.color = '#cb4344'
        super(Tag, self).save(*args, **kwargs)


