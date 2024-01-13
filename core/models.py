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
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        db_table = 'student'

# studentData = [
#     { "name": "John", "age": 20, "city": "New York", "email": "john@gmail.com" },
#     { "name": "Sam", "age": 21, "city": "New York", "email": "sam@gmail.com" },
#     { "name": "Arun", "age": 22, "city": "New York", "email": "arun@gmail.com" },
#     { "name": "Emily", "age": 23, "city": "Los Angeles", "email": "emily@gmail.com" },
#     { "name": "Michael", "age": 24, "city": "Los Angeles", "email": "michael@gmail.com" },
#     { "name": "Sophia", "age": 20, "city": "Chicago", "email": "sophia@gmail.com" },
#     { "name": "Daniel", "age": 21, "city": "Chicago", "email": "daniel@gmail.com" },
#     { "name": "Ella", "age": 22, "city": "Chicago", "email": "ella@gmail.com" },
#     { "name": "Matthew", "age": 23, "city": "San Francisco", "email": "matthew@gmail.com" },
#     { "name": "Olivia", "age": 24, "city": "San Francisco", "email": "olivia@gmail.com" },
#     { "name": "Liam", "age": 20, "city": "Seattle", "email": "liam@gmail.com" },
#     { "name": "Ava", "age": 21, "city": "Seattle", "email": "ava@gmail.com" },
#     { "name": "Lucas", "age": 22, "city": "Miami", "email": "lucas@gmail.com" },
#     { "name": "Isabella", "age": 23, "city": "Miami", "email": "isabella@gmail.com" },
#     { "name": "Mason", "age": 24, "city": "Dallas", "email": "mason@gmail.com" }
# ]

# for student in studentData:
#     Student.objects.create(**student)
