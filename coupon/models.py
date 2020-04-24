from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    parent_category = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    cat_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)


class Type(models.Model):

    name = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)


class Merchant(models.Model):

    parent_merchant = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    merchant_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)


class Coupon(models.Model):

    STATUS = [('active', 'ACTIVE'), ('inactive', 'INACTIVE')]

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    coupon_number = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25, choices=STATUS, default='active')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    rating = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    merchant = models.ForeignKey(Merchant, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category, blank=True, null=True)
    type = models.ManyToManyField(Type, blank=True, null=True)
    restriction = models.CharField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    network = models.CharField(max_length=100, blank=True, null=True)
    desc_updated = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-rating']

    def __unicode__(self):
        return '%s - %s' % (self.id, self.name)

    def __str__(self):
        return '%s - %s' % (self.id, self.name)

    def save(self, *args, **kwargs):
        super(Coupon, self).save(*args, **kwargs)


