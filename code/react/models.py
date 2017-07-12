from django.db import models

# Create your models here.
class Address(models.Model):
    country = models.CharField(max_length=140)
    region = models.CharField(max_length=140)
    locality = models.CharField(max_length=140)
    steet = models.CharField(max_length=140)
    number = models.CharField(max_length=140)

    def __str__(self):
        return self.country + ", " + self.region + ", " + self.locality


class Package(models.Model):
    name = models.CharField(max_length=140)
    max_subcompanies = models.IntegerField()

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=140)
    package = models.ManyToManyField(Package)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=140)
    nif = models.CharField(max_length=140)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=140)
    activity = models.TextField()
    type = models.ForeignKey(Type)
    childs = models.ManyToManyField('self', blank=True)


    def __str__(self):
        return self.name


class SubContracts(models.Model):
    parent = models.OneToOneField(Company, related_name='SubContracts_parent')
    child = models.OneToOneField(Company, related_name='SubContracts_child')

    class Meta:
        unique_together = ('parent', 'child')

    def __str__(self):
        return self.parent.name + " - " + self.child.name


