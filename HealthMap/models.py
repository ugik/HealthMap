from django.db import models
import datetime

class Region(models.Model):
    state = models.CharField(max_length=2, verbose_name='state', db_index=True, unique=True)
    stateName = models.CharField(max_length=25, verbose_name='state name')
    county = models.CharField(max_length=25, blank=True, db_index=True)
    imageURL = models.URLField(blank=True)
    def __unicode__(self):
        return u'state:%s (county:%s)' % (self.state, self.county)
    class Meta:
        ordering = ['state', 'county']
    
class Polyline(models.Model):
    region = models.ForeignKey('Region', db_index=True)
    lat = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='latitude')
    lng = models.DecimalField(max_digits=7, decimal_places=4, verbose_name='longitude')
    def __unicode__(self):
        return u'lat:%3.4f lng:%3.4f' % (self.lat, self.lng)
    class Meta:
        ordering = ['pk']

class Category(models.Model):
    name = models.CharField(max_length=25)
    imageURL = models.URLField(blank=True)
    def __unicode__(self):
        return self.name

class Dataset(models.Model):
    category = models.ForeignKey('Category')
    name = models.CharField(max_length=20, db_index=True)
    legend = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True)
    imageURL = models.URLField(blank=True)
    citations = models.TextField(blank=True)
    created = models.DateField(editable=False)
    updated = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not 'force_insert' in kwargs:
            kwargs['force_insert'] = False
        if not 'force_update' in kwargs:
            kwargs['force_update'] = False
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(Dataset, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Range(models.Model):
    dataset = models.ForeignKey('Dataset')
    low = models.DecimalField(max_digits=12, decimal_places=3)
    high = models.DecimalField(max_digits=12, decimal_places=3)
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=7)   # eg. #AAA000
    def __unicode__(self):
        return self.name

class Datarow(models.Model):
    dataset = models.ForeignKey('Dataset', db_index=True)
    region = models.ForeignKey('Region', db_index=True)
    value = models.DecimalField(max_digits=12, decimal_places=3)
    def color(self):
        return_color = "#FFFFFF"
        for range in self.dataset.range_set.all():
            if self.value>range.low and self.value<range.high:
                return_color = range.color
        return unicode(return_color)
    def __unicode__(self):
        return unicode(self.value)
    class Meta:
        unique_together = ("dataset", "region")

class History(models.Model):
    name = models.CharField(max_length=15)
    searched = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not 'force_insert' in kwargs:
            kwargs['force_insert'] = False
        if not 'force_update' in kwargs:
            kwargs['force_update'] = False
        self.searched = datetime.datetime.today()
        super(History, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    

