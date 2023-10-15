from django.db import models
from ipynbs.models import TestMode
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)


class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    data_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=64)


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author')

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)

# Queries 

# a1 = Author.objects.create(name="a1")

# a2 = Author.objects.create(name="a2")

# b1 = Book.objects.create(title="b1")

# b2 = Book.objects.create(title="b2")

# b1.authors.add(a1)

# b1.authors.add(a2)

# a1.book_set.all()

# b1.authors.all()